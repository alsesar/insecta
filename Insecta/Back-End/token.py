import secrets
import string
from datetime import datetime

class Codigo:
    def __init__(self, tamanho=6):
        self.tamanho = tamanho
        
    def gerar_codigo(self):
        caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        return f"{''.join(secrets.choice(caracteres) for _ in range(self.tamanho))}, {datetime.now()}"

    def enviar_codigo(self, email, novo_codigo=False):
        import sqlite3
        conn = sqlite3.connect(r'Data-Base\DTBS_teste.db')
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()

        # Verifica se o usuário existe
        usuario = cursor.execute('SELECT * FROM Usuario WHERE email = ?', (email,)).fetchone()
        if usuario is None:
            conn.close()
            return "Esse email de usuario não é valido."

        # Busca o token bruto do banco (string)
        token_bruto = cursor.execute("SELECT token FROM Usuario WHERE email = ?", (email,)).fetchone()

        # Faz o parsing manual da string do token
        if token_bruto and token_bruto[0]:
            token_str = token_bruto[0]                     # "[código, data]"
            partes = token_str.split(', ', 1)               # separa código e data
            codigo_token = partes[0]
            data_str = partes[1]
            data_token = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S.%f')
        else:
            codigo_token = None
            data_token = None

        # Se não é para gerar novo código e o token existe, verifica a validade pela data
        if (novo_codigo is False) and (codigo_token is not None):
            # Exemplo: se o token tem mais de 5 minutos (300 segundos), considera expirado
            if (datetime.now() - data_token).total_seconds() < 300:
                conn.close()
                return codigo_token          # token ainda válido
            else:
                # Token expirado, gera um novo
                novo_token = self.gerar_codigo()
                cursor.execute('UPDATE Usuario SET token = ? WHERE email = ?', (novo_token, email))
                conn.commit()
                conn.close()
                return f"Token expirado. Seu novo token é {novo_token}"


        else:
            # Nenhum token existente, gera o primeiro
            novo_token = self.gerar_codigo()
            cursor.execute('UPDATE Usuario SET token = ? WHERE email = ?', (novo_token, email))
            conn.commit()
            conn.close()
            return f"Seu novo token é {novo_token}"