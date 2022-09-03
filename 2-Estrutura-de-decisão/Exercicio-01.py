print('O MAIOR NÚMERO')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
if numero1 > numero2:
  print(f'\nO maior número é: {numero1}')
elif numero1 == numero2:
  print('\nAmbos os números são iguais!')
else:
  print(f'\nO maior número é: {numero2}')