print('COMPRAS DE FRUTAS')
kgmorango = float(input('MORANGO\nDigite quantos Kg de Morango você deseja: '))
kgmaca = float(input('\nMAÇA\nDigite quantos Kg de maça você deseja comprar: '))
if kgmorango <= 5:
  valormorango = 2.50 * kgmorango
else: 
  valormorango = 2.20 * kgmorango
if kgmaca <= 5:
  valormaca = 1.80 * kgmaca
else:
  valormaca = 1.50 * kgmaca
totalkg = kgmaca + kgmorango
valortotal = valormorango + valormaca
if totalkg > 8 or valortotal > 25:
  valortotal = valortotal - (valortotal * 10 / 100)
print(f'\nO total a se pagar é de: R${valortotal:.2f}')