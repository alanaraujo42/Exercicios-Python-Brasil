print('NÚMERO ENTRE 0 E 10')
numero = int(input('Digite uma nota entre 0 e 10: '))
while numero > 10 or numero < 0:
  print('\nValor Inválido!')
  numero = int(input('Digite uma nota entre 0 e 10: '))