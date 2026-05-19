import sqlite3
from usuario import Usuario
from verificacao import *

conn = sqlite3.connect(r'Data-Base/DTBS_teste.db')
cursor = conn.cursor()

class Cadastro:
    def __init__(self, usuario, confirmar_senha):
        self.usuario = usuario
        self.confirmar_senha = confirmar_senha
        self.campos = {
            "nome": f'{usuario.nome}', 
            "email": f'{usuario.email}', 
            "senha": f'{usuario.senha}', 
            "nome_usuario": f'{usuario.nome_usuario}', 
            "confirmar_senha": f'{confirmar_senha}'
        }

    def CadastrarUsuario(self, usuario, confirmar_senha):
        verificador = Verificacoes()
        
        campo_vazio = []
        for campo in self.campos:                        # campo é a chave ("nome", "email", etc.)
            if not verificador.VerificarCampos(self.campos[campo]):   # verifica o valor
                campo_vazio.append(f"Preencha o campo: {campo}")

        if campo_vazio:        # <-- CORRIGIDO: se a lista não estiver vazia, retorna os erros
            return campo_vazio

        # Só chega aqui se todos os campos estiverem preenchidos
        if not verificador.VerificarSenhaIgual(usuario.senha, confirmar_senha):
            return "As senhas não coincidem"
        if not verificador.VerificarSenhaForte(usuario.senha):
            return "A senha não atende aos requisitos de segurança"
        
        cursor.execute("INSERT INTO Usuario (email, nome, id_usuario, senha) VALUES (?, ?, ?, ?)", 
                      (usuario.email, usuario.nome, usuario.nome_usuario, usuario.senha))
        conn.commit()
        conn.close()
        return "Usuário cadastrado com sucesso"

# CORREÇÃO AQUI:
nome = input('nome:')
email = input('nome:')
senha = input('nome:')
id_usu = input('nome:')
novo_usuario = Usuario(f'{email}', f'{nome}', f'{id_usu}', f'{senha}')

# Criar instância da classe Cadastro
cadastro_obj = Cadastro(novo_usuario, "Senh@123")

# Chamar o método através da instância
a = cadastro_obj.CadastrarUsuario(usuario=novo_usuario, confirmar_senha="Senh@123")
print(a)