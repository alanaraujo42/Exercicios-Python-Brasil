print('ENQUETE: QUEM FOI O MELHOR JOGADRO?')
numero = int(1)
votos = int(0)
jogadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while numero != 0:
  numero = int(input('Número do jogador: '))
  while numero < 0 or numero > 23:
    print('Informe um valor entre 1 e 23. Ou 0 para sair!')
    numero = int(input('Número do jogador: '))
  if numero == 0:
    pass
  else:
    jogadores[numero - 1] += 1
    votos += 1
print('\nRESULTADO DA VOTAÇÃO:')
print(f'Foram computados {votos} votos')
print('\nJogador, Votos e Percentual:')
def percentual(votos, total):
    valor = (100 * votos) / total
    print(f'{valor:.2f}%')
contador = int(1)
maior = int(0)
for item in jogadores:
  if item == 0:
    contador += 1
    pass
  else:
    print(f'{contador}º Jogador === {item} Votos === ', end='' )
    percentual(item, votos)
    if item > maior:
      maior = item
      contador_maior = contador
      percentual_maior = (100 * item) /votos
    contador += 1
print(f'\nO melhor jogador foi o número {contador_maior}, com {maior} votos, correspondendo a {percentual_maior:.2f}% do total de votos.')
with open('resultado.txt', 'w', encoding='utf-8') as arquivo:
  arquivo.write('\nRESULTADO DA VOTAÇÃO:')
  arquivo.write(f'\nForam computados {votos} votos\n')
  arquivo.write('\nJogador, Votos e Percentual:\n')
  contador = int(1)
  maior = int(0)
  for item in jogadores:
    if item == 0:
      contador += 1
      pass
    else:
      porcentagem = (100 * item) /votos
      arquivo.write(f'{contador}º Jogador === {item} Votos === {porcentagem:.2f}%\n')
      if item > maior:
        maior = item
        contador_maior = contador
        percentual_maior = (100 * item) /votos
      contador += 1
  arquivo.write(f'\nO melhor jogador foi o número {contador_maior}, com {maior} votos, correspondendo a {percentual_maior:.2f}% do total de votos.')