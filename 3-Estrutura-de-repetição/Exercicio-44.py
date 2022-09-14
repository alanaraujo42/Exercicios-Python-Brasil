print('ELEIÇÃO PRESIDENCIAL!')
print('=== CANDIDATOS ===\n1- José\n2- João\n3- Maria\n4- Isabela\n5- Voto Nulo\n6- Voto em Branco\n0- Finalizar Programa')
voto_1 = int(0)
voto_2 = int(0)
voto_3 = int(0)
voto_4 = int(0)
voto_nulo = int(0)
voto_branco = int(0)
voto = int(1)
while voto != 0:
  voto = int(input('\nDigite o número da sua opção: '))
  if voto == 1:
    voto_1 += 1
  elif voto == 2:
    voto_2 += 1
  elif voto == 3:
    voto_3 += 1
  elif voto == 4:
    voto_4 += 1
  elif voto == 5:
    voto_nulo += 1
  elif voto == 6:
    voto_branco += 1
total_votos = voto_1 + voto_2 + voto_3 + voto_4 + voto_nulo + voto_branco
porcento_nulos = (voto_nulo * 100) / total_votos
porcento_brancos = (voto_branco * 100) / total_votos
print('\n=== Resultado ===')
print(f'Candidato 1 = {voto_1}\nCandidato 2 = {voto_2}\nCandidato 3 = {voto_3}\nCandidato 4 = {voto_4}')
print(f'\nTotal Nulos = {voto_nulo}\nTotal Brancos = {voto_branco}')
print(f'{porcento_nulos}% de votos nulos sobre o total de votos')
print(f'{porcento_brancos}% de votos em branco sobre o total de votos')