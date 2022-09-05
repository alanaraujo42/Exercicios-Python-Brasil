print('FATORIAL DE UM NÚMERO INTEIRO')
numero = int(input('Digite um número: '))
resultado = numero
while numero > 1:
  resultado = resultado * (numero - 1)
  numero = numero - 1
print(resultado)