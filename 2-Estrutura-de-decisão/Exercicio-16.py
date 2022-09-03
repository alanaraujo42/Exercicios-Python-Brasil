print('QUANTIDADE DE RAIZ DA EQUAÇÃO DO 2º GRAU')
a = float(input("Informe o valor de 'a': "))
if a == 0:
  print('\nA equação não é do 2º grau!')
else:
  b = float(input("Informe o valor de 'b': "))
  c = float(input("Informe o valor de 'c': "))
  delta = (b ** 2) - (4 * a * c)
  if delta < 0:
    print('\nA equação não possui raizes reais!')
  elif delta == 0:
    print('\nA equação possui apenas uma raiz real!')
  else: 
    print('\n1A equação possui 2 raizes reais!')