print('VERIFICAÇÃO DE NÚMERO PRIMO')
numero = int(input('Digite um número inteiro: '))
lista = list(range(2, numero))
primo = int(0)
for item in lista:
  teste = numero % item
  if teste == 0:
    primo = primo + 1
if primo != 0 or numero == 2:
  print('Não é um número primo!')
else:
  print('É um número primo!')