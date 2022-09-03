print('TRIÂNGULO')
lado1 = float(input('Digite o tamanho do 1º lado do triângulo: '))
lado2 = float(input('Digite o tamano do 2º lado do triângulo: '))
lado3 = float(input('Digite o tamanaho do 3º lado do triângulo: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
  print('\nOs tamanhos PODEM formar um trinângulo')
  if lado1 == lado2 and lado1 == lado3:
    print('O triângulo é Equilátero!')
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é Isósceles!')
  else: 
    print('O triângulo é Escaleno')
else:
  print('\nOs tamanhos NÃO PODEM formar um triângulo')