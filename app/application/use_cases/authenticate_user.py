from app.domain.authentication.services.jwt_service import generate_token
from app.domain.authentication.exceptions.exceptions_email import ExceptionsEmailNotFound
from app.domain.authentication.exceptions.exceptions_passwords import IncorrectPasswordException


class AuthenticateUserUseCase:

    def __init__(self, user_repository): 
        self.user_repository = user_repository

    def execute(self, email: str, password: str):
        # 1. Busca o usuário no banco pelo email
        user = self.user_repository.search_by_email(email)
        if not user:
            raise ExceptionsEmailNotFound()

        # 2. Verifica a senha
        if not user.password.verify(password):
            raise IncorrectPasswordException()

        # 3. (Opcional) Gerar token JWT, se necessário
        token = generate_token(user)
        return {"user": user, "token": token}
        

