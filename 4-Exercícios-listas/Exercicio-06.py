lista_media = []
aluno_maior7 = int(0)
for item in range(1, 11):
  print(f'\n=== {item}º Aluno ===')
  soma = float(0)
  for item in range(1, 5):
    nota = float(input(f'Digite a {item}º nota: '))
    soma += nota
  media = soma / 4
  lista_media.append(media)
  if media >= 7:
    aluno_maior7 += 1
print(f'\nA média dos alunos foi: {lista_media}\n{aluno_maior7} Alunos ficaram com nota maior ou igual a 7')