print('PESO IDEAL PARA HOMENES E MULHERES')
altura = float(input('Digite a sua altura: '))
pideal_h = float((72.7 * altura) - 58)
pideal_m = float((62.1 * altura) - 44.7)
sexo = input("Digite 'M' para Masculino ou 'F' para Feminino: ")
if sexo == 'M':
  print(f'O peso ideal para homens é: {pideal_h:.2f}')
else:
  print(f'O peso ideal para mulheres é: {pideal_m:.2f}')