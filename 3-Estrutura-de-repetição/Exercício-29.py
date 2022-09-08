print('LOJAS QUASE DOIS\n')
print('== TABELA DE PREÇOS ==')
listaitens = list(range(1, 51))
for item in listaitens:
  valor = item * 1.99
  print(f'{item} - R$ {valor}')