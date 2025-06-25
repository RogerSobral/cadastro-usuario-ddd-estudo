import re
import bcrypt 
from app.domain.authentication.exceptions.exceptions_passwords import StrongPasswordInvalid



class Password:
    def __init__(self, passwordInput:str):
        if not self._valid_strong_password(password=passwordInput):
            raise StrongPasswordInvalid("A senha deve conter pelo menos 6 caracteres, incluindo letra maiúscula, minúscula, número e símbolo.")
        self.__value=self._hash(passwordInput)



    # Verificação vinda do banco de dados para não converter duas vezes
    @classmethod
    def from_hashed(cls, hashed_value: bytes):
        obj = cls.__new__(cls)        
        obj.__value = hashed_value    
        return obj

    def _valid_strong_password(self,password:str):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#&*@!$]).{6,}$'
        return re.search(pattern,password) is not None
    
        
    def _hash (self,password:str)-> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify(self,passwordAttempt:str)-> bool:
        return bcrypt.checkpw(passwordAttempt.encode('utf-8'), self.__value)
    

    @property
    def value(self):
        return self.__value

    def __eq__(self, other):
        if isinstance(other,Password):
            return self.__value==other.__value
        

    def __str__(self):
        return "****"