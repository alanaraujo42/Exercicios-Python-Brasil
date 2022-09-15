print('COMPETIÇÃO DE GINÁSTICA')
atleta = input('Digite o nome do atleta: ')
contador = int(1)
soma = float(0)
while contador <= 7:
  nota = float(input(f'Digite a {contador}º nota: '))
  soma += nota
  if contador == 1:
    melhor_nota = nota
    pior_nota = nota
  else:
    if nota > melhor_nota:
      melhor_nota = nota
    elif nota < pior_nota:
      pior_nota = nota
  contador += 1
soma = soma - melhor_nota 
soma = soma - pior_nota
media = soma / 5
print(f'\n=== Resultado Final ===\nAtleta: {atleta}')
print(f'Melhor nota: {melhor_nota}\nPior nota: {pior_nota}\nMédia: {media:.2f}')