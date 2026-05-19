# #verifica se algum campo está vazio
# def VerificarCampos(self, nome, email, nome_usuario, senha, confirmar_senha):
#     if not nome or not email or not nome_usuario or not senha or not confirmar_senha:
#         return False
#     return True

# #verifica se o email ja existe no banco de dados
#     def VerificarEmailUnico(self, email):
#         cursor.execute("SELECT * FROM Usuario WHERE email = ?", (email,))
#         if cursor.fetchone():
#             return False
#         return True

#     #verifica se o nome de usuario ja existe no banco de dados
#     def VerificarNomeUsuarioUnico(self, nome_usuario):
#         cursor.execute("SELECT * FROM Usuario WHERE nome_usuario = ?", (nome_usuario,))
#         if cursor.fetchone():
#             return False
#         return True

x = ''
campos = {
            "nome": f'{x}',
            "email": f'{1+1}', 
            "senha": f'{1+1}', 
            "nome_usuario": f'{1+1}', 
            "confirmar_senha": f'{1+1}'
        }

for campo in campos:
    print(campos[campo])