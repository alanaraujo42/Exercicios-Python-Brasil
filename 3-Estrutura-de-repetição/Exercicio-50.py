print('VALOR DE H')
n = int(input('Digite um número inteiro: '))
lista = list(range(2, n + 1))
soma = int(1)
print('H = 1', end='')
for item in lista:
  print(f' + 1/{item}', end='')
  soma += 1 / item
print(f'\nO resultado é: {soma:.2f}')