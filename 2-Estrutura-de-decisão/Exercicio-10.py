print('TURNO QUE VOCÊ ESTUDA')
print('Qual turno você estuda:\nM- Matutino\nV- Vespertino\nN- Noturno')
turno = input('Digite a letra correspondente ao seu turno: ')
turno = turno.lower()
if turno == 'm':
  print('Bom Dia!')
elif turno == 'v':
  print('Boa Tarde!')
elif turno == 'n':
  print('Boa Noite!')
else:
  print('Valor Inválido!')