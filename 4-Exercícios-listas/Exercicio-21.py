carros = []
km_l = []
combustivel = []
preco = []
contador = int(1)
while contador < 6:
  print(f'\nVeículo {contador}')
  veiculo = input('Nome: ')
  km = float(input('Km por litro: '))
  carros.append(veiculo)
  km_l.append(km)
  contador += 1
for item in km_l:
  c = 1000 / item
  p = 2.25 * c
  combustivel.append(c) 
  preco.append(p)
posicao = int(1)
contador = int(0)
menor = combustivel[0]
print('\nReletorio Final')
for item in carros:
  print(f'{posicao}- {carros[contador]}', ' ' * (10 - len(carros[contador])),  f'- {km_l[contador]}', ' ' * (4 - len(str(km_l[contador]))),  f'- {combustivel[contador]:.1f} litros', ' ' * (5 - len(str(combustivel[contador]))) ,f'- R${preco[contador]:.2f}')
  if combustivel[contador] < menor:
    carro_economico = carros[contador]
  contador += 1
  posicao += 1
print(f'\nO menor consumo é do {carro_economico}')
