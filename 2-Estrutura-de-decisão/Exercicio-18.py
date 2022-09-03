print('VALIDAÇÃO DE DATA')
dia = int(input("Digite uma data no formato 'dd/mm/aaaa':\ndd: "))
mes = int(input('mm: '))
ano = int(input('aaaa: '))
bissexto = ano % 4
if ano <= 0 or mes <= 0 or mes > 12 or dia > 31 or dia <= 0:
  print('DATA INVÁLIDA!')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
  print('DATA INVÁLIDA!')
elif bissexto == 0 and mes == 2 and dia > 29:
  print('DATA INVÁLIDA!')
elif bissexto != 0 and mes == 2 and dia > 28:
  print('DATA INVÁLIDA!')
else:
  print('DATA VÁLIDA!')