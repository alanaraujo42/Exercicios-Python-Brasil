from random import choice
palavras = []
with open("6-Exercícios-com-string/Jogo-da-forca.txt", 'r') as arquivo:
  for item in arquivo:
    palavra = item.strip()
    palavras.append(palavra)
palavra_sorteada = str(choice(palavras))
palavra_teste = palavra_sorteada
forca = list("_" * len(palavra_sorteada))
erro = int(0)
while erro < 6 or forca == palavra_sorteada:
  letra = input('\nDigite uma letra: ')
  letra = letra.strip()
  if letra and letra.isalpha():
    if letra in palavra_teste:
      qtd = palavra_teste.count(letra)
      if qtd > 1:
        for x in range(0, qtd):
          p = palavra_teste.find(letra)
          forca[p] = letra
          palavra_teste = list(palavra_teste)
          palavra_teste[p] = '_'
          palavra_teste = str(''.join(palavra_teste))
        forca = str(' '.join(forca))
        print(f'A palavra é: {forca}')
        forca = forca.replace(' ', '')
        if forca == palavra_sorteada:
          break
        forca = list(forca)
      else:
        p = palavra_teste.find(letra)
        forca[p] = letra
        palavra_teste = list(palavra_teste)
        palavra_teste[p] = '0'
        palavra_teste = str(''.join(palavra_teste))
        forca = str(' '.join(forca))
        print(f'A palavra é: {forca}')
        forca = forca.replace(' ', '')
        if forca == palavra_sorteada:
          break
        forca = list(forca)
    else:
      erro += 1
      if erro < 6:
        print(f'Você errou pela {erro}º vez. Tente de Novo!')
      else:
        print(f'Você errou pela {erro}º vez e perdeu!')
  else:
    print('Digite uma letra!')
if forca == palavra_sorteada:
  print('\nParabéns! Você acertou!')