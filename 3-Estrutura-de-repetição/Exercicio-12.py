print('TABUADA 1 A 10')
numero = int(input('Digite um número de 1 a 10: '))
multiplicador = int(1)
print(f'Tabuada de {numero}:')
while multiplicador <= 10:
  resultado = numero * multiplicador
  print(f'{numero} X {multiplicador} = {resultado}')
  multiplicador = multiplicador + 1
