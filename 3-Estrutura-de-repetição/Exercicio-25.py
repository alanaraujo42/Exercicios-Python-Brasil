print('MÉDIA DE IDADES')
resposta = 'sim'
listaidade = []
while resposta == 'sim':
  idade = int(input('Digite a idade da pessoa: '))
  listaidade.append(idade)
  resposta = str.lower(input('Deseja adicionar a idada de outra pessoa (Sim ou Não)? : '))
soma = int(0)
for item in listaidade:
  soma = soma + item
media = soma / len(listaidade)
if media >= 0 and media <= 25:
  print('A turma é JOVEM!')
elif media > 25 and media <=60:
  print('A turma é ADULTA!')
else:
  print('A turma é IDOSA!')