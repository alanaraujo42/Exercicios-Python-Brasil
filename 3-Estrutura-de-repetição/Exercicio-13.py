print('POTÊNCIA')
base = float(input('Digite o 1º número: '))
expoente = float(input('Digite o 2º número: '))
contador = int(2)
resultado = base * base
while contador <= expoente - 1:
  resultado = resultado * base
  contador = contador + 1
print(f'O resultado de {base} elevado a {expoente} é: {resultado}')