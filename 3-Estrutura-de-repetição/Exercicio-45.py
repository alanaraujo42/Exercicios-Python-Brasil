print('VERIFICAÇÃO DE NOTAS')
gabarito = []
contador = int(1)
print('=== DEFININDO GABARITO ===')
while contador <= 10:
  gabarito.append(str.upper(input(f'Digite o gabarito da {contador}º questão: ')))
  contador += 1
print(gabarito)
aluno = int(0)
prova = int(1)
acertos = int(0)
continuar = 'sim'
while continuar == 'sim':
  aluno += 1
  print(f'\n=== {aluno}º Aluno ===')
  for teste in gabarito:
    resposta = str.upper(input(f'Digite a resposta da {prova}º questão: '))
    if resposta == teste:
      acertos += 1
    prova += 1
  print(f'=== CONLUÍDO {aluno}º ALUNO! ===\nTotal de Acertos: {acertos}')
  if aluno == 1:
    maior = acertos
    aluno_maior = aluno
    menor = acertos
    aluno_menor = aluno
    soma = acertos
  else:
    if acertos > maior:
      maior = acertos
      aluno_maior = aluno
    elif acertos < menor:
      menor = acertos
      aluno_menor = aluno
    soma += acertos
  acertos = int(0)
  prova = int(1)
  continuar = str.lower(input('\nOutro aluno vai usar o sistema (Sim ou Não)?: '))
media = soma / aluno
print(f'\n=== RESULTADO ===')
print(f'Maior Acerto: {aluno_maior} aluno com {maior} acerto(s)\nMenor Acerto: {aluno_menor} aluno com {menor} acerto(s)')
print(f'Total de alunos que usaram o sistema: {aluno}')
print(f'A méda das notas da turam é: {media:.2f}')