print('APROVADO OU REPROVADO V2')
nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digte a 2ª nota do aluno: '))
nota3 = float(input('Digite a 3ª nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
  print('\nAprovado com Distinção')
elif media >= 7:
  print(f'\nAPROVADO\nSua média foi: {media:.2f}')
else:
  print(f'\nREPROVADO\nSua média foi: {media:.2f}')