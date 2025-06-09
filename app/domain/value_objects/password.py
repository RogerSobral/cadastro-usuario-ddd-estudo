import re
import bcrypt 

class Password:
    def __init__(self, passwordInput:str):
        if not self._valid_strong_password(password=passwordInput):
            raise ValueError("A senha deve conter pelo menos 6 caracteres, incluindo letra maiúscula, minúscula, número e símbolo.")
        self.__value=self._hash(passwordInput)



    # Verificação vinda do banco de dados para não converter duas vezes
    @classmethod
    def from_hashed(cls, hashed_value: bytes):
        obj = cls.__new__(cls)        # Cria a instância sem chamar __init__
        obj.__value = hashed_value    # Atribui o hash diretamente
        return obj

    def _valid_strong_password(self,password:str):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#&*@!$]).{6,}$'
        if re.search(pattern,password):
            return True
        else:
            return False
        
    def _hash (self,password:str)-> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify(self,passwordAttempt:str)-> bool:
        return bcrypt.checkpw(passwordAttempt.encode('utf-8'), self.__value)
    

    @property
    def value(self):
        return self.__value
