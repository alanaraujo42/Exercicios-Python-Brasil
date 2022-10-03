def valor_pagamento(valor, atraso):
  if atraso == 0:
    return valor
  else:
    juros_dia = (atraso * 0.1) * valor / 100
    multa = valor * 3 / 100
    total = valor + multa + juros_dia
    return total
relatorio_do_dia = []
valor_prestacao = 1
while valor_prestacao != 0:
  valor_prestacao = float(input('\nDigite o valor da prestação: R$'))
  if valor_prestacao == 0: 
    break
  dias_atraso = int(input('Digite o número de dias em atraso: '))
  resultado = valor_pagamento(valor_prestacao, dias_atraso)
  print(f'O valor a ser pago é de: R${resultado}')
  relatorio_do_dia.append(resultado)
print('\nRelatorio do dia:')
print(f'Quantidades de prestações do dia: {len(relatorio_do_dia)}\nValor total das prestações pagas: R${sum(relatorio_do_dia)}')