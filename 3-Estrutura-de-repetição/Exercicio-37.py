print('SENSO DE CLIENTES DE ACADEMIA')
codigo = int(input('Digite o código do cliente: '))
altura = float(input('Digite a altura do cliente: '))
peso = float(input('Digite o peso do cliente: '))
codigo_alto = codigo
alto = altura
codigo_baixo = codigo
baixo = altura
codigo_gordo = codigo
gordo = peso
codigo_magro = codigo
magro = peso
soma_altura = altura
soma_peso = peso
contador = int(1)
while codigo != 0:
  codigo = int(input('\nDigite o código do cliente: '))
  if codigo == 0:
    break
  altura = float(input('Digite a altura do cliente: '))
  peso = float(input('Digite o peso do cliente: '))
  if altura > alto:
    alto = altura
    codigo_alto = codigo
  elif altura < baixo:
    baixo = altura
    codigo_baixo = codigo
  if peso > gordo:
    gordo = peso
    codigo_gordo = codigo
  elif peso < magro:
    magro = peso
    codigo_magro = codigo
  soma_altura += altura
  soma_peso += peso 
  contador += 1
media_altura = soma_altura / contador
media_peso = soma_peso / contador
print(f'\n=== RESULTADO ===\nCliente mais alto:\nCódigo: {codigo_alto}\nAltura: {alto}')
print(f'\nCliente mais baixo:\nCódigo: {codigo_baixo}\nAltura: {baixo}')
print(f'\nCliente mais gordo:\nCódigo: {codigo_gordo}\nPeso: {gordo}')
print(f'\nCliente mais magro:\nCódigo: {codigo_magro}\nPeso: {magro}')
print(f'\nA média de altura dos clientes é: {media_altura:.2f}\nA média de peso dos clientes é: {media_peso:.2f}')