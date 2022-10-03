from audioop import reverse


def reverso(item):
  item = str(item)
  print(f'{item[::-1]}')
numero = int(input('Digite um número inteiro: '))
reverso(numero)