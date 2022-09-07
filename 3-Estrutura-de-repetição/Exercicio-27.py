print('MÉDIA DE ALUNOS POR TURMA')
turmas = int(input('Digite a quantidade de turmas na escola: '))
listadeturams = list(range(1, turmas + 1))
soma = int(0)
for turma in listadeturams:
  alunos = int(input(f'{turma}º Turma\nDigite a quantidade de alunos dessa turam: '))
  while alunos > 40:
    print('ERRO: A turam não pode ter mais de 40 alunos. TENTE NOVAMENTE\n')
    alunos = int(input(f'{turma}º Turma\nDigite a quantidade de alunos dessa turam: '))
  soma = soma + alunos
media = soma / turmas
print(f'O número médio de alunos para cada turma é: {media}')