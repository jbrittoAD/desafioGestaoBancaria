from flask_sqlalchemy import SQLAlchemy

# Inicialização do SQLAlchemy
db = SQLAlchemy()

class Conta(db.Model):
    '''
    Classe que representa uma conta bancária.

    Atributos:
        conta_id (int): Identificador único da conta.
        saldo (float): Saldo atual da conta.
    '''
    conta_id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float)

    def __init__(self, conta_id, saldo):
        '''
        Método construtor da classe Conta.

        Args:
            conta_id (int): Identificador único da conta.
            saldo (float): Saldo inicial da conta.
        '''
        self.conta_id = conta_id
        self.saldo = saldo

    def transacao(self, forma_pagamento, valor):
        '''
        Realiza uma transação na conta.

        Args:
            forma_pagamento (str): Forma de pagamento ('D' para débito, 'C' para crédito, 'P' para PIX).
            valor (float): Valor da transação.

        Returns:
            dict: Dicionário contendo o resultado da transação.
                Se a transação for bem-sucedida, retorna {'conta_id': <conta_id>, 'saldo': <saldo_atual>}.
                Se houver algum erro, retorna {'error': <mensagem_de_erro>}, <código_de_status_HTTP>.
        '''
        # Verifica se o valor da transação é válido
        if valor <= 0:
            return {'error': 'O valor da transação deve ser maior que zero.'}, 401

        # Define a taxa de acordo com a forma de pagamento
        if forma_pagamento == 'D':
            taxa = valor * 0.03
        elif forma_pagamento == 'C':
            taxa = valor * 0.05
        elif forma_pagamento == 'P':
            taxa = 0
        else:
            return {'error': 'Forma de pagamento inválida'}, 401

        # Calcula o valor total da transação (valor + taxa)
        valor_total = valor + taxa

        # Verifica se há saldo suficiente na conta
        if self.saldo < valor_total:
            return {'error': 'Saldo insuficiente'}, 404

        # Realiza a transação e atualiza o saldo da conta
        self.saldo -= valor_total
        db.session.commit()

        # Retorna o resultado da transação
        return {'conta_id': self.conta_id, 'saldo': self.saldo}, 200
