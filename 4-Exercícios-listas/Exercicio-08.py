lista_idade = []
lista_altura = []
for item in range(1, 6):
  print(f'\n=== {item}º Pessoa ===')
  idade = int(input('Digite a sua idade: '))
  altura = float(input('Digite sua altura em m: '))
  lista_idade.append(idade)
  lista_altura.append(altura)
lista_altura.reverse()
lista_idade.reverse()
print('\nIdade: ', end='')
for item in lista_idade:
  print(item, end=' ')
print('\nAltura: ', end='')
for item in lista_altura:
  print(item, end=' ')