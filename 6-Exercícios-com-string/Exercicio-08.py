frase = str.upper(input('Digite uma frase ou palavra: '))
frase = frase.replace(' ', '')
frase_inversa = frase[::-1]
if frase_inversa == frase:
  print(f'\nA frase é um palíndromo!\n{frase_inversa}')
else:
  print(f'\nA frase não é um palíndromo!\n{frase_inversa}')