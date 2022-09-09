print('AUMENTO SALARIAL ANUALMENTE')
salario = float(input('Digite o salário inicial do funcionário: R$'))
contador = 2022 - 1996
aumento = float(1.5)
while contador != 0:
  salario = salario + (salario * aumento / 100)
  aumento = aumento * 2
  contador -= 1
print(f'O salário atual do funcionnário é: R${salario:.2f}')