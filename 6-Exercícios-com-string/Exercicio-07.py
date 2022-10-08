frase = str.casefold(input('Digite uma frase: '))
print(f'Existem {frase.count(" ")} espaços em branco na frase')
vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
print(f'As vogais "a, e, i, o, u" aparecem {vogais} vezes')