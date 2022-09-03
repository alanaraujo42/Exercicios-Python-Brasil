print('NOTA DO ALUNO')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = float((nota1 + nota2) / 2)
if media == 10:
  print('Aluno APROVADO COM DISTINÇÃO')
elif media >= 7:
  print('Aluno APROVADO')
else:
  print('Aluno REPROVADO')