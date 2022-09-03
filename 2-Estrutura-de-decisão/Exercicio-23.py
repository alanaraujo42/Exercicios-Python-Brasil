print('NÚMERO INTEIRO OU DECIMAL')
numero = float(input('Digite um número: '))
resto = numero % 1
if resto == 0.0:
  print('Número INTEIRO')
else:
  print('Número DECIMAL')