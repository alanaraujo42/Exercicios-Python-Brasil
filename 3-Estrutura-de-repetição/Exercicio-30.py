print('PANIFICADORA PÃO DE ONTEM')
precopao = float(input('Digite o preço do pão: '))
print('\n== TABELA DE PREÇOS ==')
listaitens = list(range(1, 51))
for item in listaitens:
  valor = item * precopao
  print(f'{item} - R$ {valor}')