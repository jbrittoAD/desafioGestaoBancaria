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

## Testes

Os testes podem ser feitos de algumas maneiras:
    rodando via pytest:
    No diretorio principal, deve-se rodar (para teste simplificado):
    ```
    pytest
    ```
    E para testes detalhados (mostra com mais detalhes o que está sendo testado)
    ```
    pytest -s
    ```
    De igual forma foram criados um arquivo notebook e um chamado front_simul, ambos dentro da pasta testes_codigo.
    Ambos os arquivos simulam o front-end da aplicação e realizam as operações para que seja mantida uma forma perene, como se fosse uma simulação de utilização da API. Para rodar o notebook basta rodar:
    ```
    jupyter-notebook
    ```
    E, entrar na pasta e selecionar o arquivo chamado notebook. A partir disso deve-se rodar as celulas.
    Para rodar o arquivo python basta entrar no diretório e rodar o comando:
    ```
    python front_simul.py
    ```



**Observação:** Após realizar os testes, lembre-se de disponibilizar o código no GitHub, deixar o repositório privado e adicionar como colaboradores os usuários informados pelo recrutamento.