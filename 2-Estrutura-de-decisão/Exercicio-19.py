print('LEITURA DE NÚMEROS')
numero = int(input('Digite um número inteiro menor que 1000: '))
if numero == 0:
  print('Zero é um número nulo')
elif numero == 1:
  print('1 unidade')
elif numero < 10:
  numero = str(numero)
  lista = [numero]
  unidade = lista[0]
  print(f'{unidade} unidades')
elif numero >= 10 and numero < 100:
  numero = str(numero)
  lista = [numero[0], numero[1]]
  dezena = lista[0]
  unidade = lista[1]
  if unidade == '0' and dezena != '1':
    print(f'{dezena} dezenas')
  elif unidade == '0' and dezena == '1':
    print(f'{dezena} dezena')
  elif unidade == '1' and dezena == '1':
    print(f'{dezena} dezena e {unidade} unidade')
  elif unidade == '1':
    print(f'{dezena} dezenas e {unidade} unidade') 
  elif dezena == '1':
    print(f'{dezena} dezena e {unidade} unidades')  
  else:
    print(f'{dezena} dezenas e {unidade} unidades')
elif numero > 99 and numero < 1000:
  numero = str(numero)
  lista = [numero[0], numero[1], numero[2]]
  centena = lista[0]
  dezena = lista[1]
  unidade = lista[2]
  if centena == '1' and dezena == '1' and unidade == '1':
    print('1 centena, 1 dezena e 1 unidade')
  elif centena == '1' and dezena == '1':
    if unidade == '0':
      print(f'{centena} centena e {dezena} dezena')
    else:
      print(f'{centena} centena, {dezena} dezena e {unidade} unidades')
  elif centena == '1' and unidade == '1':
    if dezena == '0':
      print(f'{centena} centena e {unidade} unidade')
    else:
      print(f'{centena} centena, {dezena} dezenas e {unidade} unidade')
  elif dezena == '1' and unidade == '1':
    print(f'{centena} centanas, {dezena} dezena e {unidade} unidade')
  elif dezena == '0' and unidade == '0':
    if centena == '1':
      print(f'{centena} centena')
    else:
      print(f'{centena} centenas')
  elif dezena == '0':
    if unidade == '1' and centena != '1':
      print(f'{centena} centenas e {unidade} unidade')
    elif centena == '1':
      print(f'{centena} centena e {unidade} unidades')
    else:
      print(f'{centena} centenas e {unidade} unidades')
  elif unidade == '0':
    if dezena == '1':
      print(f'{centena} centenas e {dezena} dezena')
    else:
      print(f'{centena} centanas e {dezena} dezenas')
  elif dezena == '1':
    print(f'{centena} centenas, {dezena} denzena e {unidade} unidades')
  elif unidade == '1':
    print(f'{centena} centenas, {dezena} denzenas e {unidade} unidade')
  elif centena == '1':
    print(f'{centena} centena, {dezena} denzenas e {unidade} unidades')
  else:
    print(f'{centena} centenas, {dezena} dezenas e {unidade} unidades')