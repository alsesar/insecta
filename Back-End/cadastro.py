import sqlite3
from usuario import Usuario

conn = sqlite3.connect('BD/DTBS_teste.db')
cursor = conn.cursor()

#verifica se algum campo está vazio
def VerificarCampos(nome, email, nome_usuario, senha, confirmar_senha):
    if not nome or not email or not nome_usuario or not senha or not confirmar_senha:
        return False
    return True

#verifica se o campo senha é igual ao campo confirmar senha
def VerificarSenhaIgual(senha, confirmar_senha):
    if senha != confirmar_senha:
        return False
    return True

#verifica se a senha possui os requisitos mínimos de segurança
def VerificarSenhaForte(senha):
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

#verifica se o email ja existe no banco de dados
def VerificarEmailUnico(email):
    cursor.execute("SELECT * FROM Usuario WHERE email = ?", (email,))
    if cursor.fetchone():
        return False
    return True

#verifica se o nome de usuario ja existe no banco de dados
def VerificarNomeUsuarioUnico(nome_usuario):
    cursor.execute("SELECT * FROM Usuario WHERE nome_usuario = ?", (nome_usuario,))
    if cursor.fetchone():
        return False
    return True

def CadastrarUsuario(usuario):
    if not VerificarCampos(usuario.nome, usuario.email, usuario.nome_usuario, usuario.senha, usuario.confirmar_senha):
        return "Preencha todos os campos"
    if not VerificarSenhaIgual(usuario.senha, usuario.confirmar_senha):
        return "As senhas não coincidem"
    if not VerificarSenhaForte(usuario.senha):
        return "A senha não atende aos requisitos de segurança"
    if not VerificarEmailUnico(usuario.email):
        return "O email já está cadastrado"
    if not VerificarNomeUsuarioUnico(usuario.nome_usuario):
        return "O nome de usuário já está em uso"
    cursor.execute("INSERT INTO Usuario (email, nome, nome_usuario, senha) VALUES (?, ?, ?, ?)", (usuario.email, usuario.nome, usuario.nome_usuario, usuario.senha))
    conn.commit()
    return "Usuário cadastrado com sucesso"

novo_usuario = Usuario("João", "joao@email.com", "jubileu", "Senh@123", "Senh@123")

a = CadastrarUsuario(novo_usuario)
print(a)