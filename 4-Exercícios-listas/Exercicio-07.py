lista = []
soma = int(0)
multiplicacao = int(1)
for item in range(1, 6):
  numero = int(input('Digite um número: '))
  lista.append(numero)
  soma += numero
  multiplicacao *= numero
print(f'\nA soma dos números é: {soma}\nA multiplicação dos números é: {multiplicacao}\nOs números são: {lista}')