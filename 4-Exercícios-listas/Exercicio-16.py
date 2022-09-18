intervalos_de_valores = [299, 399, 499, 599, 699, 799, 899, 999]
posições_de_valores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
venda_bruta = float(input('Digite a venda bruta da semana do vendedor: '))
salario = 200 + (9 * venda_bruta / 100)
contador = int(0)
for item in intervalos_de_valores:
  if salario < item:
    posições_de_valores[contador] += 1
    break
  elif salario >= 1000:
    posições_de_valores[8] += 1
    break
  contador += 1
print('=== Resultado ===')
print(f'$200 - $299: {posições_de_valores[0]} vendedor')
print(f'$300 - $399: {posições_de_valores[1]} vendedor')
print(f'$400 - $499: {posições_de_valores[2]} vendedor')
print(f'$500 - $599: {posições_de_valores[3]} vendedor')
print(f'$600 - $699: {posições_de_valores[4]} vendedor')
print(f'$700 - $799: {posições_de_valores[5]} vendedor')
print(f'$800 - $899: {posições_de_valores[6]} vendedor')
print(f'$900 - $999: {posições_de_valores[7]} vendedor')
print(f'Acima de $1000: {posições_de_valores[8]} vendedor')