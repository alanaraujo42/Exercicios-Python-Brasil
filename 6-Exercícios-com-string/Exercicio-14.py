leet_speek = {'a': '4', 'b': '|3', 'c': '¢', 'ç': '¢', 'd': '?', 'e': '€', 'é': '€', 'f': '|=', 'g': '6', 'h': '#', 'i': '!', 'j': 'j', 'k': 'X', 'l': '1', 'm': '^^', 'n': '//', 'o': '0', 'p': '|^', 'q': 'q', 'r': '|2', 's': '5', 't': '7', 'u': '(_)', 'v': '\/', 'w': '\/\/', 'x': ')(', 'y': '`/', 'z': '2' }
palavra = str.casefold(input('Digite uma frase ou palavra: '))
palavra = palavra.strip()
traducao = ''
if palavra:
  for item in palavra:
    if item == ' ':
      traducao += item
    else:
      for letra, trad in leet_speek.items():
        if letra == item:
          traducao += trad
  print(f'\nNa gráfia "leet speek" fica assim: {traducao}')
else:
  print('Digite corretamente e somente palavras')
