lista1 = []
lista2 = []
print('\n=== 1º LISTA ===')
for item in range(1, 11):
  elemento = int(input('Digite um número inteiro: '))
  lista1.append(elemento)
print('\n=== 2º LISTA ===')
for item in range(1, 11):
  elemento = int(input('Digite um número inteiro: '))
  lista2.append(elemento)
print('\n=== 3º LISTA ===')
lista3 = lista1 + lista2
print(lista3)