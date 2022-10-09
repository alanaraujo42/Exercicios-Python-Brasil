unidade = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
numeros_dez = ['onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
decimal = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',  'sessenta', 'setenta', 'oitenta', 'noventa']

numero = input('Digite um número até o 99: ')
numero = numero.strip()
if numero and numero.isnumeric() and int(numero) <= 99:
  if len(numero) > 1:
    d = int(numero[0])
    u = int(numero[1])
    if u == 0:
      numero_extenso = decimal[d - 1]
    elif d == 1:
      numero_extenso = numeros_dez[u - 1]
    else:
      numero_extenso = str(f'{decimal[d - 1]} e {unidade[u - 1]}')
  else:
    u = int(numero)
    numero_extenso = unidade[u - 1]
  print(numero_extenso.capitalize())
else:
  print('Digite apenas números e até 99!')