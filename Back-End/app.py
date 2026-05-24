from flask import Flask, request, jsonify
import uuid
from cadastro import Cadastro

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    id_usuario = data.get('id_usuario')

    if not all([nome, email, senha]):
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400

    if not id_usuario:
        id_usuario = nome

    # Gera o sufixo único (parâmetro g)
    g = str(uuid.uuid4())[:8]

    # Instancia Cadastro com os dados recebidos e executa a inserção
    cad = Cadastro(nome, email, id_usuario, senha)
    cad.usuario(g)

    return jsonify({'message': 'Cadastro realizado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)