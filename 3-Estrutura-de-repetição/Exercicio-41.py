print('DÍVIDA E SUAS PARCELAS')
valor = float(input('Digite o valo da sua dívida: R$'))
listaparcela = {1:0, 3:10, 6:15, 9:20, 12:25}
for parcela, juros in listaparcela.items():
  divida = valor + (valor * juros / 100)
  v_juros = valor * juros / 100
  v_parcela = divida / parcela
  print(f'\nValor Dívida: {divida}\nValor Juros: {v_juros}\nQuantidade de parcelas: {parcela}\nValor da Parcela: {v_parcela:.2f}')