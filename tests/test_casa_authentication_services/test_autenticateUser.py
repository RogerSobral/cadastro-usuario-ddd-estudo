import pytest
from app.application.use_cases.authenticate_user import AuthenticateUserUseCase
from app.domain.authentication.value_objects.email import Email
from app.domain.authentication.value_objects.password import Password
from app.domain.authentication.entities.user import User
from app.domain.authentication.exceptions.exceptions_email import ExceptionsEmailNotFound
from app.domain.authentication.exceptions.exceptions_passwords import IncorrectPasswordException
import os


class FakeUser (User):
    def __init__(self,id, name, email, password):
        super().__init__(name, email, password)
        self.id=id
    



class FakeRepositoryUsers:

    def dictUsers(self):
        raw_users = [
            {"id": 1, "name": "Carlos", "email": "carlos@gmail.com", "password": "1@35Aa"},
            {"id": 2, "name": "Maria",  "email": "maria@gmail.com",  "password": "835@Aa"},
            {"id": 3, "name": "Pedro",  "email": "pedro@gmail.com",  "password": "pe5@Aa"},
        ]  

        listUsers = []
        for user in raw_users:
            listUsers.append(FakeUser(user["id"], user["name"], user["email"], user["password"]))
        return listUsers

    def search_by_email(self,email) -> dict: 
        for user in self.dictUsers():
            if user.email==email:
                return user      
        raise ExceptionsEmailNotFound()
                


@pytest.fixture
def fake_repository():
    return FakeRepositoryUsers()           
    
def test_authenticate_user_successful(fake_repository):
    os.environ["JWT_SECRET"] = "uma-chave-secreta-de-teste"
    validadUser=AuthenticateUserUseCase(fake_repository)
    result=validadUser.execute("carlos@gmail.com","1@35Aa")
    user=result["user"]

    assert user.name=="Carlos"
    assert user.email=="carlos@gmail.com"
    



# Testes adicionais

# 2) Email inexistente
def test_authenticate_user_fail_email_not_found(fake_repository):
    with pytest.raises(ExceptionsEmailNotFound, match="Email não encontrado"):
        validadUser=AuthenticateUserUseCase(fake_repository)
        validadUser.execute("carl@gmail.com","1234")




# 3) Senha incorreta

def test_authenticate_user_incorrect_password(fake_repository):
    with pytest.raises(IncorrectPasswordException, match="assword invalido"):
        validadUser=AuthenticateUserUseCase(fake_repository)
        validadUser.execute("carlos@gmail.com","1@12")



# 4) Token gerado com chave ausente

# Simular ausência da SECRET_KEY no ambiente e confirmar que a exceção "Não há Key secret" é de fato levantada.



# 5) Token expirado

# Criar token com exp no passado e tentar decodificá-lo para ver se é rejeitado (isso envolve o uso de jwt.decode).