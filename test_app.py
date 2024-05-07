import pytest
from app import app, db, Conta

@pytest.fixture
def client():
    '''
    Fixture para configurar o cliente de teste.

    Configura o aplicativo Flask para modo de teste e usa um banco de dados SQLite em memória.
    '''
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_criar_conta(client):
    '''
    Testa a criação de uma conta.

    Verifica se uma conta é criada corretamente e se é possível consultar seu saldo.
    '''
    response = client.post('/conta', json={'conta_id': 1, 'valor': 500})
    assert response.status_code == 201
    print("Teste 1: Criar conta - Status code OK")

    response = client.get('/conta?conta_id=1')
    assert response.status_code == 200
    assert response.json == {'conta_id': 1, 'saldo': 500}
    print("Teste 2: Consultar conta - Status code OK e saldo correto")

def test_realizar_transacao(client):
    '''
    Testa a realização de diferentes tipos de transação.

    Verifica se transações de débito, crédito e via Pix são processadas corretamente
    e se o saldo da conta é atualizado conforme o esperado.
    '''
    client.post('/conta', json={'conta_id': 1, 'valor': 500})

    response = client.post('/transacao', json={'conta_id': 1, 'forma_pagamento': 'D', 'valor': 50})
    assert response.status_code == 200
    print("Teste 3: Transação de débito - Status code OK")

    response = client.post('/transacao', json={'conta_id': 1, 'forma_pagamento': 'C', 'valor': 100})
    assert response.status_code == 200
    print("Teste 4: Transação de crédito - Status code OK")

    response = client.post('/transacao', json={'conta_id': 1, 'forma_pagamento': 'P', 'valor': 75})
    assert response.status_code == 200
    print("Teste 5: Transação via Pix - Status code OK")

    response = client.get('/conta?conta_id=1')
    assert response.status_code == 200
    assert response.json == {'conta_id': 1, 'saldo': 268.5}
    print("Teste 6: Consultar saldo após transações - Status code OK e saldo correto")

def test_transacao_valor_acima_do_saldo(client):
    '''
    Testa uma transação com valor acima do saldo disponível na conta.

    Verifica se a transação retorna um erro de saldo insuficiente.
    '''
    client.post('/conta', json={'conta_id': 1, 'valor': 500})

    response = client.post('/transacao', json={'conta_id': 1, 'forma_pagamento': 'D', 'valor': 600})
    assert response.status_code == 404
    assert response.json == {'error': 'Saldo insuficiente'}
    print("Teste 7: Transação com valor acima do saldo - Status code e mensagem de erro OK")
