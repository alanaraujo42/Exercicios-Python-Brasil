lista_notas = []
soma_valores = float(0)
acima_da_media = int(0)
valores_menor_7 = int(0)
nota = int(0)
while nota > -1:
  nota = float(input('Digite uma nota: '))
  if nota <= -1:
    pass
  else:
    lista_notas.append(nota)
    soma_valores += nota
media = soma_valores / len(lista_notas)
print('\n=== RESULTADO ===')
print(f'Quantidade de valores lidos: {len(lista_notas)}')
print(f'Valores na ordem que foram informados: \n{lista_notas}')
print('\nValores na ordem inversa: ')
for item in reversed(lista_notas):
  print(item)
print(f'\nA soma dos valores é: {soma_valores}')
print(f'A média dos valores é: {media}')
for item in lista_notas:
  if item > media:
    acima_da_media += 1
  if item < 7:
    valores_menor_7 += 1
print(f'Quantidade de valores acima da média: {acima_da_media}')
print(f'Quantidade de valores menor que 7: {valores_menor_7}')
print('\n=== PROGRAMA ENCERRADO ===')
