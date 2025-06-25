import pytest
from app.domain.authentication.entities.user import User
from app.domain.authentication.exceptions.exceptions_email import ExceptionsEmail
from app.domain.authentication.exceptions.exceptions_passwords import StrongPasswordInvalid
from app.domain.authentication.exceptions.exceptions_name import InvalidNameError


class FakeUser (User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)



@pytest.fixture
def testableUser ():
    return FakeUser (name="carlos", email="carlos@gmail.com", password="StrongP@ss1")

def test_create_user_successful(testableUser ):
    assert testableUser .name == "carlos"
    assert testableUser .email == "carlos@gmail.com"
    assert testableUser .password.verify("StrongP@ss1")


@pytest.mark.parametrize("invalid_name", [
    "",                # Nome vazio
    "12345",          # Apenas números
    "Carlos123",      # Números misturados com letras
    "Carlos@",        # Caracteres especiais
    "C@rlos",         # Caracteres especiais
    "C",              # Nome muito curto
    "Carlos!$"       # Caracteres especiais
])

def test_name_user_falid(invalid_name):
    with pytest.raises(InvalidNameError):
         FakeUser(name=invalid_name,email="carlos@gmail.com",password="StrongP@ss1")   



@pytest.mark.parametrize("badEmail",[
    "plainaddress",                # Sem @
    "@missingusername.com",        # Sem nome de usuário
    "username@.com",               # Domínio inválido
    "username@domain..com",        # Dois pontos consecutivos
    "username@domain.c",           # Domínio muito curto
    "username@domain.c@com",       # Múltiplos @
    "username@-domain.com",        # Hífen no início do domínio
    "username@domain.com.",         # Ponto no final
    "username@domain..com",        # Dois pontos consecutivos
    "username@.com",               # Ponto antes do domínio
    "username@domain.c@com",       # Múltiplos @
    "username@domain..com",        # Dois pontos consecutivos
    "username@domain.c@com",       # Múltiplos @
    "username@domain..com",        # Dois pontos consecutivos
    "username@domain.c@com",       # Múltiplos @
    "username@domain..com",        # Dois pontos consecutivos
])


def test_create_invalid_email(badEmail):
    with pytest.raises(ExceptionsEmail):
       FakeUser(name="carlos",email=badEmail,password="StrongP@ss1") 


@pytest.mark.parametrize("bad_password",[
    "123456",       # só números
    "abcdef",       # só letras minúsculas
    "ABCDEF",       # só letras maiúsculas
    "abc123",       # sem símbolo e sem maiúscula
    "ABC123",       # sem símbolo e sem minúscula
    "abcDEF",       # sem número e sem símbolo
    "1@35A",        # menos de 6 caracteres])
])

def test_create_invalid_email(bad_password):
    with pytest.raises(StrongPasswordInvalid):
       FakeUser(name="carlos",email="carlos@gmail.com",password=bad_password) 
