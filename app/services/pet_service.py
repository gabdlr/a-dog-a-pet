import cloudinary
import cloudinary.uploader
import os
from flask import flash, Request, session
from sqlalchemy import Row, ScalarResult
from app.extensions import db
from app.models.adoptions import Adoptions
from app.models.adoption_status import AdoptionStatus
from app.models.pet import Pet
from app.models.pet_kind import PetKind
from app.utils.adoption_status import AdoptionStatusEnum
from app.utils.alert_type import AlertType
from app.utils.errors.pets.pet_register_errors import PetRegisterError
from app.utils.flash_message import FlashMessage
from app.utils.helpers import pet_sex_id_to_str
from app.utils.validators.pet_validators import PetValidators
from app.utils.validators.validators import Validators
class PetService:
    
    @staticmethod
    def adopt_pet(request: Request):
        pet_id = request.args.get('id')
        user_id = session.get('id')
        if user_id is None:
            session.clear()
            return False
        pet = PetValidators.is_valid_pet_id(pet_id)
        if pet is not None:
            if pet[0].registrar_id != user_id:
                if db.session.execute(db.select(Adoptions).filter_by(pet_id=pet_id)).one_or_none() == None:
                    adoption_statuses: ScalarResult[AdoptionStatus] = db.session.execute(db.select(AdoptionStatus)).scalars();
                    pending_status_id = None
                    
                    for adoption_status in adoption_statuses:
                        if adoption_status.name == AdoptionStatusEnum.PENDING.value:
                            pending_status_id = adoption_status.id
                    
                    if pending_status_id is not None:
                        adoption = Adoptions(
                            adopter_id=user_id,
                            pet_id=pet_id,
                            status_id=pending_status_id
                        )
                        db.session.add(adoption)
                        db.session.commit()
                        db.session.flush()
        return True
    
    @staticmethod
    def register_pet(request: Request):
        user_id = session.get('id')
        if user_id is None:
            session.clear()
            return False
        
        img = request.files['img']
        img_url = None
        if(img):
            try:
                if not Validators.allowed_file_img(img.filename):
                    raise(PetRegisterError("Invalid image format")) 
                cloudinary.config(cloud_name = os.environ.get('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
                    api_secret=os.getenv('API_SECRET'))
                upload_result = cloudinary.uploader.upload(img)
                img_url = upload_result['secure_url']
            except PetRegisterError as e:
                flash(FlashMessage(e.message, AlertType.DANGER.value ))
            except:
                print("error")

        try:
            name =  PetValidators.is_valid_name(request.form.get('name'))
            age = PetValidators.is_valid_age(request.form.get('age'))
            sex = PetValidators.is_valid_sex(request.form.get('sex')) 
            height = PetValidators.is_valid_height(request.form.get('height'))
            weight = PetValidators.is_valid_weight(request.form.get('weight'))
            kind_id = PetValidators.is_valid_type(request.form.get('type'))
            location = PetValidators.is_valid_location(request.form.get('location'))

            pet = Pet(
                name=name,
                kind_id=kind_id,
                age=age,
                img_src= img_url if img_url is not None else '/static/img/pet-placeholder.webp',
                weight=weight,
                location=location,
                sex=sex,
                height=height,
                registrar_id=user_id
            )
            db.session.add(pet)
            db.session.commit()
            db.session.flush()
        except PetRegisterError as e:
            flash(FlashMessage(e.message, AlertType.DANGER.value ))
        return True
    
    @staticmethod
    def get_pets(request: Request,results_per_page=8):            
        type = request.args.get('type')
        sex = pet_sex_id_to_str(request.args.get('sex'))
        age_from = request.args.get('age-from')
        age_to = request.args.get('age-to')
        query = db.select(Pet)
        page = request.args.get('page', 1)
        
        if sex != None:
            query = query.filter_by(sex=sex)
        if type != None:
            types = db.session.execute(db.select(PetKind.id)).scalars().all()
            if int(type) in types:
                query = query.filter_by(kind_id=type)
        if age_from != None:
            age_from = int(age_from)
            if age_from >= 0 and age_from <= 7:
                query = query.filter(Pet.age >= age_from)
        if age_to != None:
            age_to = int(age_to)
            if age_to >= 1 and age_to < 7:
                query = query.filter(Pet.age <= age_to)
        query = query.order_by(Pet.registration_date.desc())

        try:
            return db.paginate( 
                select=query, 
                page=int(page), 
                per_page=results_per_page,
                )
        except:
            return db.paginate( 
                select=query, 
                page=1, 
                per_page=results_per_page,
                )
    
    @staticmethod
    def get_options(request: Request):
        type = request.args.get('type')
        sex = request.args.get('sex')
        age_from = request.args.get('age-from')
        options = dict()
        options["type"] = PetService.get_pets_kind_options(type)
        options["sex"] = PetService.get_sex_options(sex)
        options["age_from"] = PetService.get_age_from_options(age_from)
        return options
    
    @staticmethod
    def get_pets_kind():
        return db.session.execute(db.select(PetKind)).scalars()
    
    @staticmethod
    def get_pets_kind_options(selected_kind=None):
        pet_kinds = db.session.execute(db.select(PetKind)).scalars()
        options = []
        options.append({
                "value": "",
                "text": "Type",
                "selected": selected_kind == None
            })
        options.append({
                "value": "0",
                "text": "Any",
                "selected": selected_kind == "0"
            })
        for pet_kind in pet_kinds:
            options.append({
                "value": str(pet_kind.id),
                "text": pet_kind.name,
                "selected": selected_kind == str(pet_kind.id)
            })
        PetService.selected_safeguard(selected_kind,options[0],len(options))
        return options

    @staticmethod
    def get_age_from_options(selected_year=None):
        options = []
        options.append({
                "value": "0",
                "text": "0",
                "selected": selected_year == "0" or selected_year == None
            })
        for i in range(1,7):
            options.append({
                "value": str(i),
                "text": str(i),
                "selected": selected_year == str(i)
            })
        options.append({
                        "value": "7",
                        "text": "7+",
                        "selected": selected_year == "7"
                    })
        PetService.selected_safeguard(selected_year,options[0],len(options))
        return options
    
    @staticmethod
    def get_sex_options(selected_sex=None):
        options = [
            {
                "value": "",
                "text": "Sex",
                "selected": selected_sex == None
            },
            {
                "value": "0",
                "text": "Any",
                "selected": selected_sex == "0" 
            },
                        {
                "value": "1",
                "text": "Female",
                "selected": selected_sex == "1" 
            },
            {
                "value": "2",
                "text": "Male",
                "selected": selected_sex == "2" 
            },
        ]
        PetService.selected_safeguard(selected_sex,options[0],len(options))
        return options
    
    @staticmethod
    def selected_safeguard(selected_arg: str | None, select_default, options_length: int):
        try:
            selected_arg = int(selected_arg)
            if selected_arg < 0 or selected_arg > options_length:
                select_default["selected"] = True
        except:
            select_default["selected"] = True
