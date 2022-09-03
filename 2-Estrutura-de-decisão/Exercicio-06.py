print('O MAIOR DE 3 NÚMEROS')
numero1 = float(input('Digite o 1ª número: '))
numero2 = float(input('Digite o 2ª número: '))
numero3 = float(input('Digite o 3º número: '))
maior = float(0)
if numero1 > maior or numero1 < 0:
  maior = numero1
if numero2 > maior:
  maior = numero2
if numero3 > maior:
  maior = numero3
print(f'\nO maior número é: {maior}')