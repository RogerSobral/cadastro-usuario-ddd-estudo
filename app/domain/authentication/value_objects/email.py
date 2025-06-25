import re
from app.domain.authentication.exceptions.exceptions_email import ExceptionsEmail


class Email:

    def __init__(self,email):
        if not self._valid_email(email):
            raise ExceptionsEmail("E-mail inválido !")
        self.__addressEmail=email



    def _valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+$"
        is_valid = re.match(pattern, email) is not None
        print(f"Validating email: {email}, is valid: {is_valid}")
        return is_valid

    @property
    def value(self):
        return self.__addressEmail    
    
    def __str__(self):
        return f'E-mail: {self.__addressEmail}'
    
    def __eq__(self, other):
        if isinstance(other,Email):
            return self.__addressEmail==other.__addressEmail
        return False