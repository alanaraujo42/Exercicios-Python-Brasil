print('Projeção de gastos com abono')
salario = float(1)
lista_salario = []
lista_abono = []
valor_minimo = int(0)
total_abono = float(0)
maior = float(0)
while salario != 0:
  salario = float(input('Digite o sálario do funcionário: '))
  if salario == 0:
    break
  abono = (salario * 20) / 100
  if abono < 100:
    abono = 100
  if abono == 100:
    valor_minimo += 1
  if abono > maior:
    maior = abono
  lista_salario.append(salario)
  lista_abono.append(abono)
  total_abono += abono
contador = int(0)
print('\nSalário', ' ' * 5, 'Abono')
for item in lista_salario:
  print(f'R${item}', ' ' * (10 - len(str(item))), f'R${lista_abono[contador]}')
  contador += 1
print(f'\nForam processados {len(lista_salario)} colaboradores')
print(f'Total gasto com abonos: R${total_abono}')
print(f'Valo mínimo pago a {valor_minimo} colaboradores')
print(f'Maior valor de abono pago: R${maior}')