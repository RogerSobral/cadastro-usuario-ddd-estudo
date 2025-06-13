import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from app.domain.exceptions.exceptions_name import InvalidNameError
from app.domain.entities.user import User
import pytest

def test_name_user_succefful():
    usuario=User(name="carlos",email="carlos@gmail.com",password="StrongP@ss1")
    assert usuario.name=="carlos"
    assert usuario.email=="carlos@gmail.com"
    assert usuario.password.verify("StrongP@ss1")


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
         User(name=invalid_name,email="carlos@gmail.com",password="StrongP@ss1")   
