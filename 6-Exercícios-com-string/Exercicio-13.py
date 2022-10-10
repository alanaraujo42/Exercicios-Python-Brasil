from random import choice, sample 
palavras = []
with open('6-exercícios-com-string/palavras-embaralhadas.txt', 'r', encoding='utf-8') as arquivo:
  for item in arquivo:
    palavra = item.strip()
    palavras.append(palavra)
palavra_escolhida = choice(palavras)
erro = int(0)
resposta = ''
palavra_embaralhada = sample(palavra_escolhida, len(palavra_escolhida))
palavra_embaralhada = ''.join(palavra_embaralhada)
while erro < 6 or palavra_escolhida == resposta:
  print(f'Essa é a palavra embaralhada: " {palavra_embaralhada} " ')
  resposta = input('Digite sua resposta: ')
  resposta = resposta.strip()
  if resposta == palavra_escolhida:
    break
  else:
    erro += 1
    print(f'\nVocê erro pela {erro}º vez')
print(f'\nA palavra era: {palavra_escolhida}')
if resposta == palavra_escolhida:
  print('Parabéns! Você acertou!')
elif erro == 6:
  print('Você perdeu!')
