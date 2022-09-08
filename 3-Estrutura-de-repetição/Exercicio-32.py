print('FATORIAL V.2')
numero = int(input('Digite um número inteiro: '))
listafatorial = list(range(1, numero + 1))
resultado = int(1)
for item in listafatorial:
  resultado = resultado * item
print(f'\nFatorial de: {numero}')
print(f'{numero}!', end=' = ')
for item in range(1, numero):
  print(numero, end=" * ")
  numero = numero - 1
print(f'1 = {resultado}')
