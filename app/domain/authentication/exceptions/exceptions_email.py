class ExceptionsEmail(ValueError):
    def __init__(self, message="E-mail inválido !"):
        super().__init__(message)


class ExceptionsEmailNotFound(ValueError):
    def __init__(self, message="Email não encontrado"):
        super().__init__(message)