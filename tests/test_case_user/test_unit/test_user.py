import sys
import os
import pytest
# Adiciona o caminho do módulo ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from app.domain.authentication.exceptions.exceptions_name import InvalidNameError
from app.domain.authentication.entities.user import User

class FakeUser (User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    

@pytest.fixture
def testUser ():
    usuario = FakeUser(name="carlos", email="carlos@gmail.com", password="StrongP@ss1")
    return usuario

def test_name_user_successful(testUser ):
    assert testUser .name == "carlos"
    assert testUser .email == "carlos@gmail.com"
    assert testUser .password.verify("StrongP@ss1")  


@pytest.mark.parametrize("invalid_name", [
    "",                # Nome vazio
    "12345",          # Apenas números
    "Carlos123",      # Números misturados com letras
    "Carlos@",        # Caracteres especiais
    "C@rlos",         # Caracteres especiais
    "C",              # Nome muito curto
    "Carlos!$"       # Caracteres especiais
])
def test_name_user_invalid(invalid_name):
    with pytest.raises(InvalidNameError):
        FakeUser (name=invalid_name, email="carlos@gmail.com", password="StrongP@ss1")

        