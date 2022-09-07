print('VERIFICAÇÃO DE NÚMERO PRIMO V.2')
numero = int(input('Digite um número inteiro: '))
lista = list(range(2, numero))
primo = int(0)
listadivisivel = [1]
for item in lista:
  teste = numero % item
  if teste == 0:
    primo = primo + 1
    listadivisivel.append(item)
listadivisivel.append(numero)
if primo != 0 or numero == 2:
  print('Não é um número primo!')
  print(f'Ele é divisível por {listadivisivel}')
else:
  print('É um número primo!')