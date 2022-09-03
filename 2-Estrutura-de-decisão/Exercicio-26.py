print('VENDA DE COMBUSTÍVEL')
litro = float(input('Digite quantos litros de comustível você deseja: '))
print('\nQUAL COMBUSTÍVEL VOCÊ DESEJA?\n[A]- Álcool\n[G]- Gasolina\n')
combustivel = input('Digite a letra correspondente ao combustível que deseja: ')
combustivel = combustivel.lower()
if combustivel == 'a':
  if litro <= 20:
    preco = 1.90 * litro
    total = preco - (preco * 3 / 100)
    print(f'O total a ser pago é de: R${total}')
  else:
    preco = 1.90 * litro
    total = preco - (preco * 5 / 100)
    print(f'O total a ser pago é de: R${total}')
elif combustivel == 'g':
  if litro <= 20:
    preco = 2.50 * litro
    total = preco - (preco * 4 / 100)
    print(f'O total a ser pago é de: R${total}')
  else:
    preco = 2.50 * litro
    total = preco - (preco * 6 / 100)
    print(f'O total a ser pago é de: R${total}')
else:
  print('Erro ao selecionar combustível, reinicie o programa')