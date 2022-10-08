cpf = input('Digite o seu CPF no formato (xxx.xxx.xxx-xx) :')
cpf = cpf.strip()
if cpf[3] == cpf[7] and cpf[11] == '-' and cpf.count('.') == 2 and cpf.count('-') == 1 and len(cpf) == 14:
  cpf = cpf.replace('.', '')
  cpf = cpf.replace('-', '')
  if cpf.isnumeric():
    print('CPF VÁLIDO!')
  else:
    print('CPF INVÁLIDO!')
else:
  print('CPF INVÁLIDO\nVerfique o formato digitado!')