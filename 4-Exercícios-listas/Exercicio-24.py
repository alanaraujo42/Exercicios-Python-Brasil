from random import randrange
valores = [0, 0, 0, 0, 0, 0]

for item in range(0, 100):
  x = randrange(1, 7)
  valores[x - 1] += 1
contador = int(1)
for item in valores:
  print(f'Número {contador} - {item} vezes')
  contador += 1