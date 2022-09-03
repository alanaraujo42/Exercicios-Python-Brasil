print('LOJA DE TINTAS 2.0')
area = float(input('Qual o tamanho da área a ser pintada em m²: '))
litro = float(area / 6)
lata = int(litro / 18)
galao = int(litro / 3.6)
if lata < 1:
  valorlata = float(80)
  lata = int(1)
else:
  valorlata = float(lata * 80)
if galao < 1:
  valorgalao = float(25)
  galao = int(1)
else:
  valorgalao = float(galao * 25)
print('OPÇÕES DE COMPRA:')
print(f'1ª Opção: Somente {lata} lata(s) de tintas de 18L, sendo o valor total: R${valorlata}')
print(f'2ª Opção: Somente {galao} galão(ões)) de tinta de 3,6L, sendo o valor total: R${valorgalao}')
litrofolga = float(litro + ((litro * 10) / 100))
if litrofolga <= 3.6:
  lata = int(0) 
  galao = int(1)
else:
  lata = int(0)
  galao = int(0)
  while (litrofolga > 3.6):
    galao = int(galao + 1)
    litrofolga = float(litrofolga - 3.6)
    if galao == 5:
      galao = int(0)
      lata = int(lata + 1)
valorgalao = float(galao * 25)
valorlata = float(lata * 80)
print(f'3º Opção: {lata} lata(s) de tinta de 18L e {galao} galão(ões) de tinta de 3,6L\nSendo o valor total: R${valorlata} da lata(s) e R${valorgalao} do galão(ões)')
