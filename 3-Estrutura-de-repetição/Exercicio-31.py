print('LOJAS TABAJARA - CAIXA')
sistema = int(1)
while sistema == 1:
  print('\nNOVA COMPRA')
  valor = float(1)
  soma = float(0)
  item = int(1)
  while valor != 0:
    valor = float(input(f'Produto {item}: R$ '))
    soma = soma + valor
    item = item + 1
  print(f'\nTOTAL: R${soma}')
  dinheiro = float(input('Digite o dinheiro que o cliente forneceu: R$'))
  troco = dinheiro - soma
  print(f'\nTROCO: R${troco}')