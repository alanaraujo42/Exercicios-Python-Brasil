nome = input('Digite o seu nome: ')
n = len(nome)
for i in range(0, len(nome)):
  print(nome[:n])
  n -= 1