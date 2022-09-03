print('PRODUTO MAIS BARATO')
produto1 = float(input('Digite o valor do 1º produto: R$'))
produto2 = float(input('Digite o valor do 2º produto: R$'))
produto3 = float(input('Digite o valor do 3º produto: R$'))
if produto1 < produto2 and produto1 < produto3:
  print(f'O produto mais barato é o 1º Produto, pelo preço de R${produto1}')
elif produto2 < produto1 and produto2 < produto3:
  print(f'O produto mais barato é o 2º Produto, pelo preço de R${produto2}')
else:
  print(f'O produto mais barato é o 3º Produto, pelo preço de R${produto3}')