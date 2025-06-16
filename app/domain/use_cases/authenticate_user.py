from app.domain.services.jwt_service import generate_token

"""Esse caso de uso vai:

1) Receber o e-mail e a senha como entrada=ok

2) Buscar o usuário pelo e-mail bd

3) Validar a senha com .verify() do Password()

4) Retornar o usuário autenticado ou levantar erro
"""
class AuthenticateUserUseCase:

    def __init__(self, user_repository):  # injeta o repositório de usuários, não o e-mail e senha direto
        self.user_repository = user_repository

    def execute(self, email: str, password: str):
        # 1. Busca o usuário no banco
        user = self.user_repository.search_by_email(email)
        if not user:
            raise ValueError("Email não encontrado")

        # 2. Verifica a senha
        if not user.password.verify(password):
            raise ValueError("Senha inválida")

        # 3. (Opcional) Gerar token JWT, se necessário
        token = generate_token(user)
        return {"user": user, "token": token}
        

