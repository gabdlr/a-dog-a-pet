import re
from typing import Optional

class Validators:

    @staticmethod
    def is_valid_str_and_pattern(string: Optional[str], pattern: str):
        if(isinstance(string, str)):
            regex = re.compile(pattern)
            if(regex.match(string) is not None):
                return True
        return False
    
    @staticmethod
    def is_valid_decimal(value: str):
        try:
            float(value)
            return True
        except:
            return False