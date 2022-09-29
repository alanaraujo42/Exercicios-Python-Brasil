defeitos = [0, 0, 0, 0]
percentual = []
nome_defeitos = ['1-Necessita da esfera', '2-Necessita de limpeza', '3-Necessita troca do cabo ou conector', '4-quebrado ou inutilizado']
total = int(0)
identificacao = int(1)
print('Tipos de Defeitos')
for item in nome_defeitos:
  print(item)
while identificacao != 0:
  identificacao = int(input('\nDigite o número de identificação do Mouse: '))
  tipo_defeito = int(input('Digite o número correspondente ao defeito: '))
  if tipo_defeito == 0:
    break
  defeitos[tipo_defeito - 1] += 1
  total += 1
for item in defeitos:
  porcentagem = (100 * item) / total
  percentual.append(porcentagem)
print(f'\nQuantidade de mouses: {total}')
print('\nSituação', ' ' * 32, 'Quantidade', ' ' * 10, 'Percentual')
contador = int(0)
for item in defeitos:
  print(nome_defeitos[contador], ' ' * (45 - len(nome_defeitos[contador])), item, ' ' * 17 , f'{percentual[contador]:.2f}%')
  contador += 1