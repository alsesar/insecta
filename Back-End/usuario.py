class Usuario:
    def __init__(self, email, nome, nome_usuario, senha, confirmar_senha, nivel=None, fase_id=None):
        self.email = email
        self.nome = nome
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.confirmar_senha = confirmar_senha
        self.nivel = nivel
        self.fase_id = fase_id
