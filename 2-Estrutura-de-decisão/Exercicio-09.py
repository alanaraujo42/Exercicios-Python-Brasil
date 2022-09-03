print('ORDEM DECRESCENTE')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite outro número: '))
# Se número 1 e número 2 forem iguais
if numero1 == numero2:
  if numero1 > numero3:
    primeiro = numero1
    segundo = numero2
    terceiro = numero3
  if numero1 == numero3:
    primeiro = numero1
    segundo = numero2
    terceiro = numero3
  if numero1 < numero3:
    primeiro = numero3
    segundo = numero1
    terceiro = numero2
# Se número 1 e número 3 forem iguais
elif numero1 == numero3:
  if numero1 > numero2:
    primeiro = numero1
    segundo = numero3
    terceiro = numero2
  if numero1 == numero2:
    primeiro = numero1
    segundo = numero2
    terceiro = numero3
  if numero1 < numero2:
    primeiro = numero2
    segundo = numero1
    terceiro = numero3
# SE TODOS OS NÚMEROS FOREM IGUAIS
elif numero2 == numero3:
  if numero2 > numero1:
    primeiro = numero2
    segundo = numero3
    terceiro = numero1
  if numero2 == numero1:
    primeiro == numero1
    segundo == numero2
    terceiro == numero3
  if numero2 < numero1:
    primeiro = numero1
    segundo = numero2
    terceiro = numero3
elif numero1 == numero2 and numero1 == numero3:
  primeiro = numero1
  segundo = numero2
  terceiro = numero3
# SE NENHUM NÚMERO FOR IGUAL
else:
  primeiro = numero1
  if numero2 > primeiro and numero2 > numero3:
    primeiro = numero2
    if numero1 < numero3:
      terceiro = numero1
      segundo = numero3
    else:
      terceiro = numero3
      segundo = numero1
# SE NÚMERO 2 FOR O MAIOR 
  elif numero3 > primeiro and numero3 > numero2:
    primeiro = numero3
    if numero2 < numero1:
      terceiro = numero2
      segundo = numero1
    else: 
      terceiro = numero1
      segundo = numero2
# SE NÚMERO 3 FOR O MAIOR
  elif numero2 < numero3:
    terceiro = numero2
    segundo = numero3
  else: 
    terceiro = numero3
    segundo = numero2
# SE NÚMERO 1 FOR O MAIOR
print(f'O 1º número é: {primeiro}\nO 2º número é: {segundo}\nO 3º número é: {terceiro}')