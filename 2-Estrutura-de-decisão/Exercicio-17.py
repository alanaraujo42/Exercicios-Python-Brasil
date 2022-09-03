print('ANO BISSEXTO')
ano = int(input('Digite o número de um ano: '))
bissexto = ano % 4
if bissexto == 0:
  print(f'O ano {ano} é BISSEXTO!')
else: 
  print(f'O ano {ano} NÃO É BISSEXTO!')