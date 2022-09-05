print('SÉRIE DE FIBONACCI')
termo = int(input('Digite um número até a posições que deseja: '))
ultimo = int(1)
penultimo = int(0)
contador = int(1)
while contador <= termo:
  print(ultimo)
  meio = ultimo
  ultimo = ultimo + penultimo
  penultimo = meio
  contador = contador + 1