print('ELEIÇÃO E ELITÕRES')
eleitores = int(input('Digite o número total de eleitores: '))
listadeeleitores = list(range(1, eleitores + 1))
candidato1 = int(0)
candidato2 = int(0)
candidato3 = int(0)
print('CANDIDATOS\n[1] - Candidato A\n[2] - Candidato B\n[3] - Candidato C')
for eleitor in listadeeleitores:
  voto = int(input(f'\nEleitor {eleitor}\nDigite o número correspondente ao candidato que deseja votar: '))
  if voto == 1:
    candidato1 = candidato1 + 1
  elif voto == 2:
    candidato2 = candidato2 + 1
  elif voto == 3:
    candidato3 = candidato3 + 1
print(f'\nRESULTADO\nCandidato A = {candidato1} votos\nCandidato B = {candidato2} votos\nCandidato C = {candidato3} votos')