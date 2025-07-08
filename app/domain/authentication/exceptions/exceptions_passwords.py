
class StrongPasswordInvalid(ValueError):

    def __init__(self, mensage="Password fraco"):
        super().__init__(mensage)


class  IncorrectPasswordException(ValueError):
    def __init__(self, mensage="Password invalido"):
        super().__init__(mensage)
