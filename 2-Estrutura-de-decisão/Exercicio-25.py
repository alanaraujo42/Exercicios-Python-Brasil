print('INVESTIGAÇÃO CRIMINAL')
pergunta1 = int(input('[1]SIM [2]NÃO\nVocê telefonou para a vitma? '))
afirmação = 0
if pergunta1 == 1:
  afirmação = afirmação + 1
pergunta2 = int(input('Você esteve no local do crime? '))
if pergunta2 == 1:
  afirmação = afirmação + 1
pergunta3 = int(input('Você mora perto da vítima? '))
if pergunta3 == 1:
  afirmação = afirmação + 1
pergunta4 = int(input('Você devia para a vítima? '))
if pergunta4 == 1:
  afirmação = afirmação + 1
pergunta5 = int(input('Você já trabalhou com a vítima? '))
if pergunta5 == 1:
  afirmação = afirmação + 1
if afirmação == 2:
  print('Você é SUSPEITO')
elif afirmação == 3 or afirmação == 4:
  print('Você é CÚMPLICE')
elif afirmação == 5:
  print('Você é o ASSASSINO')
else:
  print('Você é INOCENTE')