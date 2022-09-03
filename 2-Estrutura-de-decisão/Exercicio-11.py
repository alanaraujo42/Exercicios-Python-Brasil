print('AUMENTO DE SALÁRIO')
salario = float(input('Digite o valor do salário: '))
if salario <= 280:
  percentual = 20
  valoraumento = float(salario * 20 / 100)
  novosalario = float(salario + valoraumento)
elif salario > 280 and salario < 700:
  percentual = 15
  valoraumento = float(salario * 15 /100)
  novosalario = float(salario + valoraumento)
elif salario >= 700 and salario < 1500:
  percentual = 10
  valoraumento = float(salario * 10 /100)
  novosalario = float(salario + valoraumento)
elif salario >= 1500:
  percentual = 5
  valoraumento = float(salario * 5 /100)
  novosalario = float(salario + valoraumento)
print(f'\nO salário antes do reajuste era: R${salario}')
print(f'O percentual de aumento aplicado foi de: {percentual}%')
print(f'O valor do aumento foi de: R${valoraumento}')
print(f'O novo salário é de: R${novosalario}')