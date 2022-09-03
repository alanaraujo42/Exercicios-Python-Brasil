print('NOTAS DO SEMESTRE')
nota1 = float(input('Digite a 1º nota do aluno: '))
nota2 = float(input('Digite a 2º nota do aluno: '))
media = (nota1 + nota2) / 2
if media >= 9 and media <=10:
  conceito = 'A'
  mensagem = 'APROVADO'
elif media >= 7.5 and media < 9:
  conceito = 'B'
  mensagem = 'APROVADO'
elif media >= 6 and media < 7.5:
  conceito = 'C'
  mensagem = 'APROVADO'
elif media >= 4 and media < 6:
  conceito = 'D'
  mensagem = 'REPROVADO'
elif media < 4:
  conceito = 'E'
  mensagem = 'REPROVADO'
print(f'\nA 1º nota foi: {nota1}\nA 2ª nota foi: {nota2}')
print(f'A média das notas foi: {media}\nVocê ficou com {conceito} e está {mensagem}')