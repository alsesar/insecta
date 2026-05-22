import json
import sqlite3
from pathlib import Path

class Inicial:
    
    def __init__(self, email='ffelipeessantoss@hotmail.com'):
        self.email = email
        self.usuario = None
        
        conn = sqlite3.connect(r'Data-Base\DTBS_teste.db')  # Use uma barra só
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE email = ?', (email,))
        self.usuario = cursor.fetchone()
        conn.close()
    
    def dados(self):
        # Verifica se usuário existe
        if self.usuario is None:
            print(f"Usuário com email {self.email} não encontrado!")
            return None  # Retorna None explicitamente
        
        # Cria a pasta se não existir (caminho corrigido)
        Path(r'..\Front-End').mkdir(exist_ok=True)
        
        # Escreve o JSON
        with open(r'..\Front-End\pagina_usuario.json', 'w', encoding='utf-8') as f:
            usuario_dict = {
                'id_usuario': self.usuario[1],
                'nome': self.usuario[2],
                'email': self.usuario[0],
            }                
            json.dump(usuario_dict, f, ensure_ascii=False, indent=2)
        
        # Retorna o dicionário para ser usado
        return usuario_dict

# # Teste
# import time
# t = time.time()
# for i in range((10**5)):
#     geeg = Inicial()
#     dado = geeg.dados()
#     # Agora vai mostrar o dicionário ou None
# f = time.time()
# tt = f-t
# print(tt)
