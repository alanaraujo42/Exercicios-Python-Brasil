print('LOJA DE TINTAS')
area = float(input('Qual o tamanho da área a ser pintada em m²: '))
litro = float(area / 3)
lata = int(litro / 18)
if lata < 1:
  valorlata = float(80)
  lata = int(1)
else:
  valorlata = float(lata * 80)
print(f'\nA quantidade de latas de tinta que você precisa é de: {lata} lata')
print(f'O valor total é de: R${valorlata} \nVolte Sempre!!')