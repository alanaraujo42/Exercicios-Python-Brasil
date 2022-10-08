frase1 = input('Digite uma frase: ')
frase2 = input('Digite outra frase: ')
tamanho_frase1 = len(frase1)
tamanho_frase2 = len(frase2)
print(f'\nTamanho de "{frase1}": {tamanho_frase1} caracteres')
print(f'Tamanho de "{frase2}": {tamanho_frase2} caracteres')
if tamanho_frase1 == tamanho_frase2:
  print('As duas strings são de tamanhos iguais')
else:
  print('As duas strings são de tamanho diferentes')
if frase1 == frase2:
  print('As duas strings possuem conteúdo iguais')
else:
  print('As duas strings possuem conteúdo diferentes')