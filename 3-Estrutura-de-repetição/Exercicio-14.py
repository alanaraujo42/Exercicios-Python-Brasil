print('10 NÚMEROS, PARES OU IMPARES')
numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))
numero4 = int(input('Digite o 4º número: '))
numero5 = int(input('Digite o 5º número: '))
numero6 = int(input('Digite o 6º número: '))
numero7 = int(input('Digite o 7º número: '))
numero8 = int(input('Digite o 8º número: '))
numero9 = int(input('Digite o 9º número: '))
numero10 = int(input('Digite o 10º número: '))
listanumero = [numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8, numero9, numero10]
par = 2 % 2
numeropar = int(0)
numeroimpar = int(0)
for numero in listanumero:
  teste = numero % 2
  if teste == par:
    numeropar = numeropar + 1
  else:
    numeroimpar = numeroimpar + 1
print(f'\nExistem {numeropar} números pares\nExistem {numeroimpar} números impares')