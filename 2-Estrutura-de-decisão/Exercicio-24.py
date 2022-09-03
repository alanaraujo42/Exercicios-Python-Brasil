print('OPERAÇÕES DE 2 NÚMEROS')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print('OPERAÇÕES:\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão')
operação = int(input('Digite o número correspondente a operação que você deseja realizar: '))
if operação == 1:
  resultado = numero1 + numero2
elif operação == 2:
  resultado = numero1 - numero2
elif operação == 3:
  resultado = numero1 * numero2
elif operação == 4:
  resultado = numero1 / numero2
print(f'O resultado é: {resultado:.2f}')
par = resultado % 2
resto = resultado % 1
if par == 0:
  print('\nO resultado é PAR')
elif par != 0 and resto != 0.0:
  print('\nO resultado NÃO É PAR NEM IMPAR, por ser decimal')
else: 
  print('\nO resultado é IMPAR')
if resultado == 0:
  print('O número é NULO')
elif resultado > 0:
  print('O resultado é POSITIVO')
else:
  print('O resultado é NEGATIVO')
if resto == 0.0:
  print('O resultado é INTEIRO')
else: 
  print('O resultado é DECIMAL')