from random import randrange
def lancar_dado():
  dado = randrange(2, 13)
  return dado
dado = lancar_dado()
print(f'Seu número foi: {dado}')
if dado == 7 or dado == 11:
  print('Você tirou um NATURAL e ganhou! Parabéns!')
elif dado == 2 or dado == 3 or dado == 12:
  print('Você tirou um "CRAPS" e perdeu!')
else:
  print('Você tirou um "PONTO"!')
  ponto = dado
  while True:
    dado = lancar_dado()
    print(f'Seu número foi: {dado}')
    if dado == ponto:
      print('Parabéns! Você venceu!')
      break
    elif dado == 7:
      print('Você perdeu!')
      break
print('FIM')