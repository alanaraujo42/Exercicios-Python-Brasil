print('N TERMOS DE UMA SÉRIE')
numero = int(input('Digite um número inteiro: '))
n = int(1)
m = int(1)
soma = n / m
print('\nS = 1/1', end='')
while n != numero:
  n += 1
  m += 2
  print(f' + {n}/{m}', end='')
  soma += n / m
print(f'\nA soma da série é: {soma:.2f}')