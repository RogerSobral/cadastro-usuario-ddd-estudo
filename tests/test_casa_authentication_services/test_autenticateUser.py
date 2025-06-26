import pytest
from app.application.use_cases.authenticate_user import AuthenticateUserUseCase
from app.domain.authentication.value_objects.email import Email
from app.domain.authentication.value_objects.password import Password
from app.domain.authentication.entities.user import User


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
        raise ValueError("Erro ao procurar o email")
                


@pytest.fixture
def fake_repository():
    return FakeRepositoryUsers()           
    
def test_authenticate_user_successful(fake_repository):
    validadUser=AuthenticateUserUseCase(fake_repository)
    result=validadUser.execute("carlos@gmail.com","1@35Aa")
    user=result["user"]

    assert user.name=="Carlos"
    assert user.email=="carlos@gmail.com"
    