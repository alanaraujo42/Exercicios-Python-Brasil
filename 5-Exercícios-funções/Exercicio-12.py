from random import sample
def embaralhamento(item):
  novo_nome = sample(item, len(item))
  novo_nome = ''.join(novo_nome)
  print(novo_nome)
nome = str.lower(input('Digite uma palavra: '))
embaralhamento(nome)
