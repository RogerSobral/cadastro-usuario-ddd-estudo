
class StrongPasswordInvalid(ValueError):

    def __init__(self, mensage="Password fraco"):
        super().__init__(mensage)