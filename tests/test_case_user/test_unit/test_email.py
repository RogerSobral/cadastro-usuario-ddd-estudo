import pytest
from app.domain.authentication.value_objects.email import Email
from app.domain.authentication.exceptions.exceptions_email import ExceptionsEmail

def test_valid_email():
    # Cria um objeto Email válido
    email = Email("teste@example.com")

def test_integridade_email_create():
    email = Email("teste@example.com")
    assert email.value == "teste@example.com"
    
def test_return_String_email():
    email = Email("teste@example.com")
    assert str(email) == "E-mail: teste@example.com"


@pytest.mark.parametrize("value_test_email_invalid", [
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


def test_invalid_email_raises_error(value_test_email_invalid):
    with pytest.raises(ExceptionsEmail):
        Email(value_test_email_invalid)


def test_email_equality():
    email1 = Email("user@example.com")
    email2 = Email("user@example.com")
    email3 = Email("outro@example.com")

    # Dois objetos Email com o mesmo endereço devem ser iguais
    assert email1 == email2

    # Dois objetos Email com endereços diferentes devem ser diferentes
    assert email1 != email3

    # Um objeto Email não é igual a uma string (mesmo que contenha o mesmo email)
    assert email1 != "user@example.com"
