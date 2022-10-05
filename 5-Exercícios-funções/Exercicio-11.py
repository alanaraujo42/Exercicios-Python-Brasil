def mes_por_extenso(dia, mes, ano):
  mes_extenso = ['Janeiro', 'Feveriro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outurbro', 'Novembro', 'Dezembro']
  mes = mes_extenso[mes - 1]
  dia = str(f'{dia} de')
  ano = str(f'de {ano}')
  data = str(f'{dia} {mes} {ano}')
  return data 
dia = int(input('Digite o dia (dd): '))
mes = int(input('Digite o mês (mm): '))
ano = int(input('Digite o ano (aaaa): '))
bissexto = ano % 4
if dia > 31 or mes > 12 or ano < 1:
  print('Data Inválida!')
elif mes == 4 or mes == 6 or mes == 11 or mes == 9 and dia > 30:
  print('Data Inválida!')
elif bissexto == 0 and dia > 29:
  print('Data Inválida!')
elif bissexto != 0 and dia > 28:
  print('Data Inválida!')
else:
  data = mes_por_extenso(dia, mes, ano)
  print(data)