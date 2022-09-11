print('CONTAGEM DE NÚMEROS')
numero = float(1)
intervalo0_25 = int(0)
intervalo26_50 = int(0)
intervalo51_75 = int(0)
intervalo76_100 = int(0)
while numero >= 0:
  numero = float(input('Digite um número: '))
  if numero > 0 and numero <= 25:
    intervalo0_25 += 1
  elif numero > 25 and numero <=50:
    intervalo26_50 += 1
  elif numero > 50 and numero <= 75:
    intervalo51_75 += 1
  elif numero > 75 and numero <= 100:
    intervalo76_100 += 1
print(f'\nNo intervalo de 0 a 25 tem {intervalo0_25} números')
print(f'\nNo intervalo de 26 a 50 tem {intervalo26_50} números')
print(f'\nNo intevalo de 51 a 75 tem {intervalo51_75} números')
print(f'\nNo intevalo de 76 a 100 tem {intervalo76_100} números')