print('DIA DA SEMANA')
numero = float(input('Digite um número: '))
if numero == 1:
  dia = 'Domingo'
elif numero == 2:
  dia = 'Segunda-Feira'
elif numero == 3:
  dia = 'Terça-Feira'
elif numero == 4:
  dia = 'Quarta-Feira'
elif numero == 5:
  dia = 'Quinta-Feira'
elif numero == 6:
  dia = 'Sexta-Feira'
elif numero == 7:
  dia = 'Sábado'
else: 
  dia = 'Valor Inválido!'
print(dia)