print('CARDÁPIO DE LANCHONETE')
resposta = 'sim'
soma = float(0)
while resposta == 'sim':
  codigo = int(input('\nDigite o código do item: '))
  quantidade = int(input('Digite a quantidade: '))
  if codigo == 100:
    valor = quantidade * 1.20
    soma += valor
  elif codigo == 101:
    valor = quantidade * 1.30
    soma += valor
  elif codigo == 102:
    valor = quantidade * 1.50
    soma += valor
  elif codigo == 103:
    valor = quantidade * 1.20
    soma += valor
  elif codigo == 104:
    valor = quantidade * 1.30
    soma += valor
  elif codigo == 105:
    valor = quantidade * 1
    soma += valor
  print(f'\nTotal do Item: {valor}\nTotal do Pedido: {soma}')
  resposta = str.lower(input('\nDeseja adicionar outro item (Sim ou Não)? '))
