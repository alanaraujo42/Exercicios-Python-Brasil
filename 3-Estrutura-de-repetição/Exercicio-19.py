print('MENOR, MAIOR E SOMA DOS NÚMEROS V.2')
numero1 = float(input('Digite o 1º número: '))
while numero1 < 0 or numero1 > 1000:
  print('ERRO: Só pode número entre 0 e 1000\nTente novamente\n')
  numero1 = float(input('Digite o 1º número: '))

numero2 = float(input('Digite o 2º número: '))
while numero2 < 0 or numero2 > 1000:
  print('ERRO: Só pode número entre 0 e 1000\nTente novamente\n')
  numero2 = float(input('Digite o 2º número: '))

numero3 = float(input('Digite o 3º número: '))
while numero3 < 0 or numero3 > 1000:
  print('ERRO: Só pode número entre 0 e 1000\nTente novamente\n')
  numero3 = float(input('Digite o 3º número: '))

listanumeros = [numero1, numero2, numero3]
maior = numero1
menor = numero1
soma = int(0)
for numero in listanumeros:
  if numero > maior:
    maior = numero
  elif numero < menor:
    menor = numero
  soma = soma + numero
print(f'\nO menor valor é {menor}\nO maior valor é {maior}\nA soma dos número é: {soma}')