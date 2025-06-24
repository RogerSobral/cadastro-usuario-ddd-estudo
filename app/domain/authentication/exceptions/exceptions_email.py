class ExceptionsEmail(ValueError):
    def __init__(self, message="E-mail inválido !"):
        super().__init__(message)