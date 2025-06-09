import re
from value_objects.password import Password
from value_objects.email import Email

class User:

    def __init__(self,name,email,password):
        self.__name=self._valid_name(name)
        self.__email=Email(email)
        self.__password=Password(password).value  # Pode lançar ValueError aqui

    @property
    def name(self):
        return self.__name
    
    def _valid_name(self,newName:str)->bool:
        if not newName.isalpha():
              raise ValueError("Nome inválido, deve ser somente letras.")
        else:
            return newName
        
    @name.setter
    def name(self,newName):
        self.__name=self._valid_name(newName)

    @property
    def email(self):
        return self.__email

        


        
