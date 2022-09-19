atleta = input('Digite o nome do atleta: ')
while atleta != '':
  lista_saltos = []
  soma = float(0)
  for item in range(1, 6):
    salto = float(input(f'{item}º Salto: '))
    lista_saltos.append(salto)
    soma += salto
  media = soma / 5
  print(f'\nPrimeiro Salto: {lista_saltos[0]}m')
  print(f'Segundo Salto: {lista_saltos[1]}m')
  print(f'Terceiro Salto: {lista_saltos[2]}m')
  print(f'Quarto Salto: {lista_saltos[3]}m')
  print(f'Quinto Salto: {lista_saltos[4]}m')
  print('\nResultado Final:')
  print(f'Atleta: {atleta}')
  print(f'Saltos: {lista_saltos[0]} - {lista_saltos[1]} - {lista_saltos[2]} - {lista_saltos[3]} - {lista_saltos[4]}')
  print(f'Média dos Saltos: {media}m')
  atleta = input('\nDigite o nome do atleta: ')
