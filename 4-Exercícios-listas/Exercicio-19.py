print(''''
Qual o melhor sistema operacional para uso em servidores?

As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')
resposta = int(1)
enquete = [0, 0, 0, 0, 0, 0]
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos_total = int(0)
while resposta != 0:
  resposta = int(input('Digite o número correspondente a sua resposta: '))
  while resposta < 0 or resposta > 6:
    print('Número inválido -- Tente Novamente')
    resposta = int(input('Digite o número correspondente a sua resposta: '))
  enquete[resposta - 1] += 1
  votos_total += 1
print('\nSistema Operacional     Votos   %  ')
print('-' * 36)
contador = int(0)
maior = int(0)
for item in enquete:
  porcentagem = (item * 100) / votos_total
  print(f'{sistemas[contador]}', ' ' * (23 - len(sistemas[contador])), item, ' ' * 4, f'{porcentagem:.1f}%')
  if item > maior:
    maior = item
    sistema_maior = sistemas[contador]
    porcentagem_maior = porcentagem
  contador += 1
print('-' * 29)
print('Total', ' ' * 18, votos_total)
print(f'\nO Sistema Operacional mais votado foi o {sistema_maior}, com {maior} votos, correspondendo a {porcentagem_maior:.1f}% dos votos.')