print('O MAIOR E O MENOR DE 3 NÚMEROS')
numero1 = float(input('Digite o 1ª número: '))
numero2 = float(input('Digite o 2ª número: '))
numero3 = float(input('Digite o 3º número: '))
maior = float(0)
menor = float(0)
if numero1 > maior or numero1 < 0:
  maior = numero1
if numero2 > maior:
  maior = numero2
  menor = numero1
elif numero2 < numero1:
  menor = numero2
if numero3 > maior:
  maior = numero3
elif numero3 < menor:
  menor = numero3
print(f'\nO MAIOR número é: {maior}')
print(f'O MENOR número é {menor}')