
# Teste da classe Codigo para gerar e gerenciar tokens
from token import Codigo
from datetime import datetime

# Instancia a classe
codigo = Codigo(tamanho=8)  # Token de 8 caracteres

# Teste 1: Gerar um código simples
print("="*50)
print("🔑 TESTE DE GERAÇÃO DE TOKEN")
print("="*50)
token_simples = codigo.GerarCodigo()
print(f"Token gerado: {token_simples}")
print(f"Tamanho: {len(token_simples)} caracteres\n")

# Teste 2: Enviar código para um usuário existente (primeira vez)
print("="*50)
print("📧 TESTE DE ENVIO PARA USUÁRIO EXISTENTE")
print("="*50)
resultado1 = codigo.EnviarCodigo("alice@gmail.com")
print(f"Resultado: {resultado1}\n")

# Teste 3: Solicitar novamente (sem forçar novo_codigo) - deve retornar o mesmo
print("="*50)
print("🔄 TESTE DE REENVIO (MESMO TOKEN)")
print("="*50)
resultado2 = codigo.EnviarCodigo("alice@gmail.com")
print(f"Resultado: {resultado2}\n")

# Teste 4: Forçar novo código
print("="*50)
print("🆕 TESTE DE NOVO TOKEN (FORÇADO)")
print("="*50)
resultado3 = codigo.EnviarCodigo("alice@gmail.com", novo_codigo=True)
print(f"Resultado: {resultado3}\n")

# Teste 5: Usuário inexistente
print("="*50)
print("❌ TESTE COM USUÁRIO INVÁLIDO")
print("="*50)
resultado4 = codigo.EnviarCodigo("inexistente@email.com")
print(f"Resultado: {resultado4}\n")

# Teste 6: Gerar para outro usuário
print("="*50)
print("👥 TESTE COM OUTRO USUÁRIO")
print("="*50)
resultado5 = codigo.EnviarCodigo("carlos@email.com", novo_codigo=True)
print(f"Resultado: {resultado5}\n")

print("✅ Todos os testes concluídos!")