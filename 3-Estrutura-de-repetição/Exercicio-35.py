print('DESCOBRINDO NÚMEROS PRIMOS')
numero = int(input('Digtie um número inteiro: '))
listadenumeros = list(range(1, numero + 1))
listaprimos = []
primo = int(0)
for item in listadenumeros:
  listateste = list(range(1, item + 1))
  primo = int(0)
  for numeroteste in listateste:
    teste = item % numeroteste
    if teste == 0 and item != 1 and numeroteste != 1 and numeroteste != item:
      primo = int(1)
  if primo == 0 and item != 1:
    listaprimos.append(item)
print(f'\nOs números primos são:\n{listaprimos}')