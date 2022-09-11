print('ALUNO MAIS ALTO E ALUNO MAIS BAIXO')
aluno_numero = int(input('Digite o número do aluno: '))
altura = float(input('Digite a altura do aluno em centimetros: '))
numero_baixo = aluno_numero
baixo = altura
numero_alto = aluno_numero
alto = altura
contador = int(1)
while contador < 10:
  aluno_numero = int(input('\nDigite o número do aluno: '))
  altura = float(input('Digite a altura do aluno em centimetros: '))
  if altura > alto:
    numero_alto = aluno_numero
    alto = altura
  elif altura < baixo:
    numero_baixo = aluno_numero
    baixo = altura
  contador += 1
print(f'\n=== Aluno mais Alto ===\nNúmero: {numero_alto}\nAltura: {alto}')
print(f'\n=== Aluno mais Baixo ===\nNúmero: {numero_baixo}\nAltura: {baixo}')