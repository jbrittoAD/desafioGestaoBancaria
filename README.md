# Sistema de Gestão Bancária

Este é um projeto de desafio técnico que consiste na criação de um sistema de gestão bancária por meio de uma API, composta por dois endpoints: "/conta" e "/transacao". O endpoint "/conta" é responsável por criar e fornecer informações sobre o número da conta e o saldo, enquanto o endpoint "/transacao" realiza diversas operações financeiras.

## Funcionalidades

- **Criar Conta:** O endpoint "/conta" permite criar uma nova conta com saldo inicial.
- **Consultar Saldo:** O endpoint "/conta" também permite consultar o saldo de uma conta existente.
- **Realizar Transação:** O endpoint "/transacao" realiza operações financeiras como débito, crédito e Pix, aplicando taxas específicas para cada forma de pagamento.

## Especificações

- Os endpoints seguem um padrão de entrada e saída em formato JSON.
- As formas de pagamento são representadas pelas siglas: P (Pix), C (Cartão de Crédito) e D (Cartão de Débito).
- Todas as contas não possuem limite de cheque especial, ou seja, não é permitido ter saldo negativo.

## Executando as Operações

1. Validar se uma conta existe.
2. Criar uma conta com saldo inicial de R$ 500.
3. Consultar o saldo dela.
4. Efetuar uma compra no valor de R$ 50 utilizando a opção de débito.
5. Executar uma compra de R$ 100 usando a opção de crédito.
6. Realizar uma transferência via Pix no valor de R$ 75.

## Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite

## Como Executar a Aplicação

1. Clone este repositório em sua máquina local:

```
git clone <https://github.com/jbrittoAD/desafioGestaoBancaria>
```

2. Navegue até o diretório do projeto:

```
cd sistema-gestao-bancaria
```

3. Instale as dependências do Python:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
python app.py
```

5. Acesse os endpoints conforme necessário, utilizando a ferramenta ou cliente HTTP de sua preferência (por exemplo, curl ou Postman).

Claro, aqui está o texto revisado para o README.md do git:

## Testes

Os testes podem ser realizados de várias maneiras:

### Testes com pytest:
Para executar testes básicos, no diretório principal, execute:
```bash
pytest
```
Para testes mais detalhados (exibindo mais informações sobre o que está sendo testado), execute:
```bash
pytest -s
```

### Testes com arquivos de simulação:
Foram criados dois arquivos de simulação na pasta `testes_codigo`: um arquivo de notebook e um chamado `front_simul.py`.
Esses arquivos simulam o front-end da aplicação e realizam operações para manter uma forma perene, como se fosse uma simulação de utilização da API.

#### Para executar o arquivo notebook:
Execute o seguinte comando:
```bash
jupyter-notebook
```
Em seguida, navegue até a pasta e selecione o arquivo chamado `notebook.ipynb`. Depois disso, execute as células conforme necessário.

#### Para executar o arquivo Python:
Entre no diretório e execute o seguinte comando:
```bash
python front_simul.py
```
