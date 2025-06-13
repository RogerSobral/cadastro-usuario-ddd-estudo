import re
from app.domain.value_objects.password import Password
from app.domain.value_objects.email import Email
from app.domain.exceptions.exceptions_name import InvalidNameError

class User:

    def __init__(self,name,email,password):
        self.__name=self._valid_name(name)
        self.__email=Email(email)# Pode lançar ValueError aqui
        self.__password=Password(password) # Pode lançar ValueError aqui

    @property
    def name(self):
        return self.__name
    
    def _valid_name(self,newName:str)->bool:
        pattern= r"^[A-Za-zÀ-ÿÇç\s'-]+$"
        if not newName or len(newName) < 2:  # Verifica se o nome é vazio ou muito curto
            raise InvalidNameError("Nome inválido, deve ter pelo menos 2 caracteres.")
        if not re.match(pattern, newName):  # Verifica se o nome contém apenas letras e espaços
            raise InvalidNameError("Nome inválido, deve conter apenas letras.")
        return newName
        
    @name.setter
    def name(self,newName):
        self.__name=self._valid_name(newName)

    @property
    def email(self):
        return self.__email.value

        
    @property
    def password(self):
        return self.__password

        
