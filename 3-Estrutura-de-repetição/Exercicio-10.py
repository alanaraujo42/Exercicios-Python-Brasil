numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digtie o 2º número: '))
if numero1 > numero2:
  maior = numero1
  menor = numero2
elif numero2 > numero1:
  maior = numero2
  menor = numero1
if numero1 == numero2:
  print('Os 2 números são iguais!')
elif menor + 1 != maior:
  menor = menor + 1
  while menor < maior:
    print(menor)
    menor = menor + 1
else:
  print('Não tem números inteiros entre eles!')