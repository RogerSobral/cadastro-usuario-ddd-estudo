# import pytest
# import re

# class User:

#     def __init__(self,name,email,password):
#         self.name=name
#         self.email=email
#         self.password=password

    
# class SimpleUseReposit:
#     def __init__(self):
#         self.users= []

#     def find_by_email(self,email):
#         return next((u for u in self.users if u.email==email),None)
    
#     def save(self,user):
#         self.users.append(user)
#         return True

# #  Create Case of test

# class  CreateUseCaseUser:
#     def __init__(self,user_repo):
#         self.user_repo=user_repo

#     def execute(self, user):
        
#         if not self._valid_email(user.email):
#             raise ValueError("E-mail inválido")

#         if not self._valid_password(user.password):
#             raise ValueError("Senha fraca")

#         if self.user_repo.find_by_email(user.email):
#             raise ValueError("Usuário já existe")

#         return self.user_repo.save(user)
    
#     def _valid_email(self, email):
#         pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
#         return re.match(pattern, email) is not None

#     def _valid_password(self, password):
#         return len(password) >= 8
    

# # case tests
# def test_create_user_success():
#     repo = SimpleUseReposit()
#     use_case = CreateUseCaseUser(user_repo=repo)

#     user = User(name="Ana", email="ana@email.com", password="senha1234")
#     result = use_case.execute(user)

#     assert result is True
#     assert len(repo.users) == 1
#     assert repo.users[0].email == "ana@email.com"

# def test_create_user_duplicate_email():
#     repo = SimpleUseReposit()
#     use_case = CreateUseCaseUser(user_repo=repo)

#     user1 = User(name="Ana", email="ana@email.com", password="senha1234")
#     use_case.execute(user1)

#     user2 = User(name="Ana 2", email="ana@email.com", password="outrasenha")
#     with pytest.raises(ValueError, match="Usuário já existe"):
#         use_case.execute(user2)

# def test_create_user_invalid_email():
#     repo = SimpleUseReposit()
#     use_case = CreateUseCaseUser(user_repo=repo)

#     user = User(name="Carlos", email="email-invalido", password="senha1234")
#     with pytest.raises(ValueError, match="E-mail inválido"):
#         use_case.execute(user)

# def test_create_user_weak_password():
#     repo = SimpleUseReposit()
#     use_case = CreateUseCaseUser(user_repo=repo)

#     user = User(name="Bruna", email="bruna@email.com", password="123")
#     with pytest.raises(ValueError, match="Senha fraca"):
#         use_case.execute(user)

