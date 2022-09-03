print('PROMOÇÃO DE CARNES')
print('\nESCOLHA UM TIPO DE CARNE:\n[1] - File Duplo\n[2] - Alcatra\n[3] - Picanha')
carne = int(input('Digite o número correspondente a carne que você deseja: '))
kg = float(input('Digite quantos Kg de carne você deseja: '))
if carne == 1:
  tipocarne = 'File Duplo'
  if kg <= 5:
    preco = 4.90 * kg
  else:
    preco = 5.80 * kg
elif carne == 2:
  tipocarne = 'Alcatra'
  if kg <= 5:
    preco = 5.90 * kg
  else:
    preco = 6.80 * kg
elif carne == 3:
  tipocarne = 'Picanha'
  if kg <=5 :
    preco = 6.90 * kg
  else:
    preco = 7.80 * kg
print('Deseja utilizar o cartão Tabajara? \n[1] SIM OU [2] NÃO')
cartao = int(input('Digite o número correspondente a sua escolha: '))
if cartao == 1:
  desconto = preco * 5 / 100
  precopagar = preco - desconto
  tipopagamento = 'COM CARTÃO TABAJARA'
else: 
  tipopagamento = 'SEM CARTÃO TABAJARA'
  desconto = int(0)
  precopagar = preco
print(f'\nCUPOM FISCAL\nTIPO DE CARNE: {tipocarne}\nQUANTIDADE DE CARNE: {kg}Kg\nPREÇO TOTAL: R${preco:.2f}\nTIPO DE PAGAMENTO: {tipopagamento}\nVALOR DO DESCONTO: R${desconto:.2f}\nVALOR A PAGAR: R${precopagar:.2f}')