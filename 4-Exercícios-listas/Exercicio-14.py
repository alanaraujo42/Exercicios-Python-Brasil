perguntas = ['Você telefonou para a vítma? ', 'Esteve no local do crime? ', 'Mora perto da vítma? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? ']
respostas = []
print('== INVESTIGAÇÃO ==')
print('Responda com SIM ou NÃO')
for item in perguntas:
  resposta = str.lower(input(item))
  if resposta == 'sim':
    respostas.append(resposta)
if len(respostas) == 2:
  print('\nVocê é suspeito!')
elif len(respostas) == 3 or len(respostas) == 4:
  print('\nVocê é cúmplice!')
elif len(respostas) == 5:
  print('\nVocê é o assasino!')
else:
  print('\nVocê é inocente!')
