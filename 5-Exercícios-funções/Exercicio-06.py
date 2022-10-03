def conversao(hora):
  if hora == 00:
    hora = 12
    turno = 'A'
    return hora, turno
  elif hora > 12:
    hora = hora - 12
    turno = "P"
    return hora, turno
  elif hora == 12:
    turno = 'P'
    return hora, turno
  else:
    turno = 'A'
    return hora, turno
def saida(hora, minuto, turno):
  if turno == 'A': turno = 'A.M'
  else: turno = 'P.M'
  print(f'{hora}:{minuto} {turno}')
continuidade = 'sim'
while continuidade == 'sim':
  hora = int(input('\nDigite as horas em formato 24h: '))
  minuto = int(input('Digite os minutos: '))
  hora, turno = conversao(hora)
  saida(hora, minuto, turno)
  continuidade = str.lower(input('Deseja continuar (Sim ou Não): '))
