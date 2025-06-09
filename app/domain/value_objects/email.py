import re

class Email:

    def __init__(self,email):
        if not self._valid_email(email):
            raise ValueError("E-mail inválido !")
        self.__addressEmail=email



    def _valid_email(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern,email) is not None

    @property
    def value(self):
        return self.__addressEmail    
    
    def __str__(self):
        return f'E-mail: {self.__addressEmail}'
    
    def __eq__(self, other):
        if isinstance(other,Email):
            return self.__addressEmail==other.__addressEmail
        return False