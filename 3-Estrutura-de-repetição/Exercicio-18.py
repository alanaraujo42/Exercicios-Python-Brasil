print('MENOR, MAIOR E SOMA DOS NÚMEROS')
numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))
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