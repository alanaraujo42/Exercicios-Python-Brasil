lista = []
lista_par = []
lista_impar = []
for item in range(1, 21):
  numero = int(input('Digite um número inteiro: '))
  lista.append(numero)
  teste = numero % 2
  if teste == 0:
    lista_par.append(numero)
  else:
    lista_impar.append(numero)
print(f'\nTodos os números: {lista}\nNúmeros Pares: {lista_par}\nNúmeros Impares: {lista_impar}')