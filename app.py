from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from acounts import Conta, db  # Importe a classe Conta e o objeto db do arquivo models.py


app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicialize o SQLAlchemy com a aplicação Flask

# Defina o IP e a porta desejados para a aplicação
host = '127.0.0.0'  # IP para escutar em todas as interfaces
port = 5000       # Porta desejada


# Rota para criar uma nova conta
@app.route('/conta', methods=['POST'])
def criar_conta():
    '''
    Rota para criar uma nova conta.

    Espera um JSON com os campos 'conta_id' e 'valor'.
    Se a conta já existe, atualiza o saldo.
    Se a conta não existe, cria uma nova.
    Retorna um JSON com o 'conta_id' e 'saldo' da conta criada ou atualizada.
    '''
    data = request.get_json()
    conta_id = data.get('conta_id')
    valor = data.get('valor')
    conta = Conta.query.filter_by(conta_id=conta_id).first()
    if conta:
        conta.saldo = valor
    else:
        nova_conta = Conta(conta_id=conta_id, saldo=valor)
        db.session.add(nova_conta)
    db.session.commit()

    return jsonify({'conta_id': conta_id, 'saldo': valor}), 201


# Rota para realizar uma transação
@app.route('/transacao', methods=['POST'])
def realizar_transacao():
    '''
    Rota para realizar uma transação.

    Espera um JSON com os campos 'conta_id', 'forma_pagamento' e 'valor'.
    Verifica se a conta existe.
    Chama o método 'transacao' da classe Conta para processar a transação.
    Retorna o resultado da transação em formato JSON.
    '''
    data = request.get_json()
    forma_pagamento = data.get('forma_pagamento')
    conta_id = data.get('conta_id')
    valor = data.get('valor')
    conta = Conta.query.filter_by(conta_id=conta_id).first()
    if not conta:
        return jsonify({'error': 'Conta não encontrada'}), 404
    return conta.transacao(forma_pagamento, valor)


# Rota para obter informações da conta
@app.route('/conta', methods=['GET'])
def obter_conta():
    '''
    Rota para obter informações da conta.

    Espera o parâmetro 'conta_id' na query string.
    Retorna um JSON com o 'conta_id' e 'saldo' da conta encontrada, ou um erro se a conta não existir.
    '''
    conta_id = request.args.get('conta_id')
    conta = Conta.query.filter_by(conta_id=conta_id).first()
    if not conta:
        return jsonify({'error': 'Conta não encontrada'}), 404
    return jsonify({'conta_id': conta.conta_id, 'saldo': conta.saldo}), 200


# Função para criar o banco de dados e suas tabelas
def create_db():
    '''
    Função para criar o banco de dados e suas tabelas.
    '''
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    # Cria o banco de dados se não existir
    create_db()
    # Executa o aplicativo Flask
    app.run(host=host, port=port, debug=True)
