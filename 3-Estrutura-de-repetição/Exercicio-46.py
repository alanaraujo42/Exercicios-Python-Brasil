print('COMPETIÇÃO DE SALTOS')
atleta = input('Digite o nome do atleta: ')
while atleta != '':
  lista = []
  contador = int(1)
  while contador <= 5:
    salto = float(input(f'Digite a distância do {contador}º salto em metros: '))
    lista.append(salto)
    if contador == 1:
      maior = salto
      menor = salto
    else:
      if salto > maior:
        maior = salto
      elif salto < menor:
        menor = salto
    contador += 1
  contador = int(1)
  print(f'\nAtleta: {atleta}\n')
  for item in lista:
    print(f'{contador}º Salto: {item}m')
    contador += 1
  print(f'\nMelhor Salto: {maior}m')
  print(f'Pior Salto: {menor}m')
  lista.remove(maior)
  lista.remove(menor)
  media = float((lista[0] + lista[1] + lista[2]) / 3)
  print(f'Média dos demais saltos: {media:.2f}m')
  print(f'\nResultado Final:\n{atleta}: {media:.2f}m')
  print('\n=== Finalização ===')
  atleta = input('\nDigite o nome de outro atleta: ')