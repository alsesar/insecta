class Verificacoes:
    @staticmethod
    def VerificarSenhaForte(senha):          # sem self
        if len(senha) < 8:
            return False
        if not any(c.isupper() for c in senha):
            return False
        if not any(c.islower() for c in senha):
            return False
        if not any(c.isdigit() for c in senha):
            return False
        if not any(c in "!@#$%^&*()_+-=[]{}|;':\"<>,./?" for c in senha):
            return False
        return True

    @staticmethod
    def VerificarSenhaIgual(senha, confirmar_senha):   # sem self
        return senha == confirmar_senha

    @staticmethod
    def VerificarCampos(campo):               # sem self
        return bool(campo and campo.strip())