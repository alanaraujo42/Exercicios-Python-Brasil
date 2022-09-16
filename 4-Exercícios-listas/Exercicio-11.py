lista1 = []
lista2 = []
lista3 = []
print('\n=== 1º LISTA ===')
for item in range(1, 11):
  elemento = int(input('Digite um número inteiro: '))
  lista1.append(elemento)
print('\n=== 2º LISTA ===')
for item in range(1, 11):
  elemento = int(input('Digite um número inteiro: '))
  lista2.append(elemento)
print('\n=== 3º LISTA ===')
for item in range(1, 11):
  elemento = int(input('Digite um número inteiro: '))
  lista3.append(elemento)
print('\n=== LISTAS INTERCALADAS ===')
lista4 = lista1 + lista2 + lista3
print(lista4)