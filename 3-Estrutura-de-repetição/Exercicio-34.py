print('NÚMEROS PRIMOS E CRIPTOGRAFIA')
numero = int(input('Digite um número inteiro: '))
lista = list(range(1, numero + 1))
primo = int(0)
for item in lista:
  teste = numero % item
  if teste == 0 and item != 1 and item != numero:
    primo = int(1)
if primo == 1 or numero == 1:
  print('\nEsse número NÂO É PRIMO!')
else:
  print('\nEsse número É PRIMO!')