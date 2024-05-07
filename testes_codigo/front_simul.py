import requests

# URL base da sua aplicação Flask
base_url = 'http://localhost:5000'

# Função para validar se uma conta existe
def validar_conta(conta_id):
    response = requests.get(f'{base_url}/validar_conta?conta_id={conta_id}')
    if response.status_code == 200:
        print("A conta existe.")
    else:
        print("A conta não existe.")

# Função para criar uma nova conta com saldo inicial de R$ 500
def criar_conta(conta_id):
    response = requests.post(f'{base_url}/conta', json={'conta_id': conta_id, 'valor':500.0})
    print(response.json())

# Função para consultar o saldo de uma conta
def consultar_saldo(conta_id):
    response = requests.get(f'{base_url}/conta?conta_id={conta_id}')
    print(response.json())

# Função para efetuar uma compra no valor especificado usando débito
def comprar_debito(conta_id, valor):
    response = requests.post(f'{base_url}/transacao', json={'conta_id': conta_id, 'valor': valor, 'forma_pagamento':'D'})
    print(response.json())

# Função para efetuar uma compra no valor especificado usando crédito
def comprar_credito(conta_id, valor):
    response = requests.post(f'{base_url}/transacao', json={'conta_id': conta_id, 'valor': valor, 'forma_pagamento':'C'})
    print(response.json())

# Função para realizar uma transferência via Pix
def transferencia_pix(conta_id, valor):
    response = requests.post(f'{base_url}/transacao', json={'conta_id': conta_id, 'valor': valor, 'forma_pagamento':'P'})
    print(response.json())

# Executando as operações
conta_id = 1

validar_conta(conta_id)
criar_conta(conta_id)
consultar_saldo(conta_id)
comprar_debito(conta_id, 50)
comprar_credito(conta_id, 100)
transferencia_pix(conta_id, 75)
