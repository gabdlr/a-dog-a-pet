from flask import Request
from app.extensions import db
from app.models.pet_kind import PetKind

class PetService:
    
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
    def selected_safeguard(selected_arg, select_default, options_length):
        if selected_arg is not isinstance(selected_arg, int) or selected_arg < 0 or selected_arg > len(options_length):
            select_default["selected"] = True