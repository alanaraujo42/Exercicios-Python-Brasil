print('COLEÇÃO DE CDs')
quantidadecds = int(input('Digite a quantidade de CDs que possui: '))
listacds = list(range(1, quantidadecds + 1))
soma = float(0)
for cd in listacds:
  valor = float(input(f'{cd}º CD\nDigite o valor do CD: R$ '))
  soma = soma + valor
media = soma / quantidadecds
print(f'\nO total investido na coleção de CDs é de R${soma:.2f}\nO valo médio gasto para cada CD é de R${media:.2f}')
