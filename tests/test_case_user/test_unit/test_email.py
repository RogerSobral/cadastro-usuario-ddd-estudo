import pytest
from app.domain.value_objects.email import Email

def test_valid_email():
    # Cria um objeto Email válido
    email = Email("teste@example.com")
    
    # Verifica se o atributo value está correto
    assert email.value == "teste@example.com"
    
    # Verifica se o método __str__ retorna a string esperada
    assert str(email) == "E-mail: teste@example.com"

def test_invalid_email_raises_error():
    # Usar "with pytest.raises" para capturar o ValueError esperado
    with pytest.raises(ValueError) as exc_info:
        Email("sobral.com")
    # opcional: verificar a mensagem do erro
    assert str(exc_info.value) == "E-mail inválido !"  # Ajuste conforme a mensagem que você usa na sua classe Email

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
