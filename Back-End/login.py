import json
import sqlite3
from pathlib import Path

class Login:
    def __init__(self):
        caminho_json = r'..\\Front-End\\login.json'
        if not Path(caminho_json).exists():
            raise FileNotFoundError(f"Arquivo {caminho_json} não encontrado!")
        with open(caminho_json, 'r', encoding='utf-8') as f:
            self.dados = json.load(f)

    def usuario(self):
        conn = sqlite3.connect(r'Data-Base\\DTBS_teste.db')
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE email = ? AND senha = ?',(self.dados['email'], self.dados['senha']))
        validacao = cursor.fetchone() is not None
        conn.close()
        return validacao

# Teste

import time 
t = time.time()
for i in range((10**5)):
    login = Login()
    dado = login.usuario()
f = time.time()
tt = f-t
print(tt)


