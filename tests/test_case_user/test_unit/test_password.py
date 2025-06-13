from app.domain.value_objects.password import Password
from app.domain.exceptions.exceptions_passwords import StrongPasswordInvalid
import pytest
import bcrypt

def test_valid_password_succefful():
   
    password=Password("1@35Aa")



def test_valid_password_invalid():
    # caso não va ele vai lançar um erro
    with pytest.raises(StrongPasswordInvalid):
        Password("1@35A")


@pytest.mark.parametrize("invalid_password",[
    "123456",       # só números
    "abcdef",       # só letras minúsculas
    "ABCDEF",       # só letras maiúsculas
    "abc123",       # sem símbolo e sem maiúscula
    "ABC123",       # sem símbolo e sem minúscula
    "abcDEF",       # sem número e sem símbolo
    "1@35A",        # menos de 6 caracteres])
])

def test_valid_password_invalid_parametrize(invalid_password):
    with pytest.raises(StrongPasswordInvalid):
        Password(invalid_password)

def test_from_hashed_DB():
    password="1@35Aa"
    hashPassword=bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    obj=Password.from_hashed(hashPassword)
    assert isinstance(obj,Password)
    assert obj.value==hashPassword
    assert obj.verify(password)
