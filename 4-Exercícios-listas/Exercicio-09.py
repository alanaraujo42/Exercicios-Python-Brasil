soma = int(0)
for item in range(1, 11):
  numero = int(input(f'Digite o {item}º número inteiro: '))
  quadrado = numero ** 2
  soma += quadrado
print(f'\nA soma dos quadrados dos números é: {soma}')