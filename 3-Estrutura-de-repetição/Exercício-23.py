print('NÚMEROS PRIMOS ENTRE 1 E...')
numero = int(input('Digite um número inteiro: '))
lisadenumeros = list(range(1, numero + 1))
numerosprimos = []
quantidadedivisão = int(0)
if numero == 1:
  print('\nO número 1 NÃO é primo\nFoi realizada 1 divisão')
else:
  for numeroteste in lisadenumeros:
    primo = int(0)
    listateste = list(range(1, numeroteste + 1))
    for itemteste in listateste:
      teste = numeroteste % itemteste
      if teste == 0 and numeroteste != 1 and itemteste != numeroteste and itemteste !=1:
        primo = primo + 1
      quantidadedivisão = quantidadedivisão + 1
    if primo == 0 and numeroteste != 1:
      numerosprimos.append(numeroteste)
  print(f'\nOs números primos entre 1 e {numero} são: \n{numerosprimos}\nForam realizadas {quantidadedivisão} divisões')