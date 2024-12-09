from app.extensions import db
from app.models.pet_kind import PetKind
from app.utils.errors.pets.pet_register_errors import PetRegisterError
from app.utils.helpers import pet_sex_id_to_str
from app.utils.validators.validators import Validators

class PetValidators:
    
    @staticmethod
    def is_valid_name(name: str|None):
        if Validators.is_valid_str_and_pattern(name,'^[A-Za-z ]{2,255}$'):
            return name
        raise PetRegisterError("Invalid pet name")
    
    @staticmethod
    def is_valid_age(age: str|None):
        try:
            if int(age) >= 0:
                return age
        except:
            raise PetRegisterError("Invalid age")
        raise PetRegisterError("Invalid age")

    @staticmethod
    def is_valid_weight(w: str|None):
        if w is None:
            return None
        if Validators.is_valid_decimal(w) and float(w) >= 0:
            return w
        raise PetRegisterError("Invalid pet weight")

    @staticmethod
    def is_valid_height(h: str|None):
        if h is None:
            return None
        if Validators.is_valid_decimal(h) and float(h) >= 0:
            return h
        raise PetRegisterError("Invalid pet height")

    @staticmethod
    def is_valid_sex(sex: str|None):
        pet_sex = pet_sex_id_to_str(sex)
        if pet_sex is None:
            raise PetRegisterError("Invalid pet sex")
        return pet_sex

    @staticmethod
    def is_valid_type(pet_type: str|None):
        INVALID_MSG = "Invalid pet type"
        if pet_type is None:
            raise PetRegisterError(INVALID_MSG)
        types = db.session.execute(db.select(PetKind)).scalars()
        try:
            for type in types:
                if int(pet_type) == type.id:
                    return pet_type
        except:
            raise PetRegisterError(INVALID_MSG) 
        raise PetRegisterError(INVALID_MSG) 
        
    @staticmethod
    def is_valid_location(location: str|None):
        if location is not None:
            if Validators.is_valid_str_and_pattern(location,'^[A-Za-z ]{2,255}$'):
                return location
        raise PetRegisterError("Invalid location")