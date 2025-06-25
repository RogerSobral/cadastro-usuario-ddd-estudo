import pytest
from app.application.use_cases.authenticate_user import AuthenticateUserUseCase

class FakeRepositoryUsers:
    pass


def test_authenticate_user_successful():
    validadUser=AuthenticateUserUseCase().execute()
    