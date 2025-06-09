from app.domain.value_objects.password import Password

def test_valid_password():
    # caso não va ele vai lançar um erro
    password=Password("1@35Aa")
    if not password.value==Password().from_hashed("1@35Aa"):
        raise ValueError("Erro ao cadastrar a senha")

