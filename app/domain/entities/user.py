import re
from value_objects.password import Password
class User:

    def __init__(self,name,email,password):
        self.__name=self._valid_name(name)
        self.__email=self._valid_email(email)
        self.__password=Password(password)  # Pode lançar ValueError aqui

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,newName):
        self._valid_name(newName)

    @property
    def email(self):
        return self.__email

    @name.setter
    def email(self,newEmail):
        self._valid_email(newEmail)
        

    def _valid_email(self, newEmail)->bool:
        pattern=r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if re.search(pattern,newEmail):
            self.__email=newEmail
            return True
        else:
            return False
        
    def _valid_name(self,newName:str)->bool:
        if newName.isalpha():
            self.__name=newName
            return True
        else:
            return False