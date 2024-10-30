import requests
import json
import datetime


today = datetime.datetime.now()
moedas = ['USD-BRL', 'EUR-BRL', 'BTC-BRL']
exit = True

ui = '''
+==========================+
|         COTAÇÕES         |
+==========================+
|     {0} {1}:{2}:{3}     |
+--------------------------+
|Escoha uma opção:         |
|   [1] - Dollar           |
|   [2] - Euro             |
|   [3] - BitCoin          |
|   [0] - Sair             |
|                          |
|                          |
|                          |
|         by Doug Barcelos |   
+--------------------------+
'''.format(datetime.date.today().strftime("%d/%m/%y"), today.hour, today.minute, today.second)

def req(op):
    req = requests.get('https://economia.awesomeapi.com.br/last/' + moedas[op-1])
    cotacao = json.loads(req.text)
    moeda = moedas[op-1].replace('-', '')
    cotacao_moeda = cotacao[moeda]['high']
    valor = float(cotacao_moeda)
    valor_formatado = f'R$ {valor:_.2f}'
    valor_formatado = valor_formatado.replace('.', ',').replace('_', '.')

    print(f"A Cotação do {cotacao[moeda]['name'][:-16]} é R$: {valor_formatado}")

while exit:
    print(ui)
    op = int(input('-> '))
    if op == 0:
        exit = False
    else:
        req(op)