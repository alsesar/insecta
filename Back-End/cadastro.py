import json
import sqlite3
from usuario import Usuario
from verificacao import *

class Cadastro:
    def __init__(self):
       with open(r'..\Front-End\cadastro.json', 'r', encoding='utf-8') as f:
        self.dados = json.load(f)

    def usuario(self):
        conn = sqlite3.connect(r'Data-Base\DTBS_teste.db')
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()

        cadastro =self.dados
        cursor.execute("INSERT INTO Usuario (email, nome, id_usuario, senha) VALUES (?, ?, ?, ?)", 
                       (cadastro["email"], cadastro["nome"], cadastro["id_usuario"], cadastro["senha"])) 
        conn.commit()
        conn.close()

cadastro = Cadastro()
dado = cadastro.usuario()
print(dado)