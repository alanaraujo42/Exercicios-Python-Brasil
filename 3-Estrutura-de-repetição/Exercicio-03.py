print('VALIDAÇÃO DE INFORMAÇÕES')
nome = input('Digite um nome: ')
while len(nome) <= 3:
  print('ERRO: O nome tem que ter mais de 3 caracteres!\nTente novamenteo\n')
  nome = input('Digite um nome: ')
else:
  print('Nome Válido!\n')

idade = int(input('Digite uma idade: '))
while idade > 150 or idade < 0:
  print('ERRO: A idade tem que ser entre 0 e 150\nTente Noamente\n')
  idade = int(input('Digite uma idade: '))
else:
  print('Idade Válida!\n')

salario = float(input('Digite o valor de um salário: '))
while salario <= 0:
  print('ERRO: O Salário tem que ser maior que 0\nTente Novamente\n')
  salario = float(input('Digite o valor de um salário: '))
else:
  print('Salário Válido!\n')

sexo = input('Digite [F] para Feminino ou [M] para Masculino: ')
sexo = sexo.lower()
while sexo != 'f' and sexo != 'm':
  print('ERRO: Sexo Inválido!\nTente Novamente\n')
  sexo = input('Digite [F] para Feminino ou [M] para Masculino: ')
  sexo = sexo.lower()
else:
  print('Sexo Válido!\n')

print('Estado Civil\n[S]- Solteiro(a)\n[C]- Casado(a)\n[V]- Viúvo(a)\n[D]- Divorciado(a)')
estadocivil = input('Digite a letra correspondente ao seu estado civil: ')
estadocivil = estadocivil.lower()
while estadocivil != 's' and estadocivil != 'c' and estadocivil != 'v' and estadocivil != 'd':
  print('ERRO: Estado Civil Inválido\nTente novamente\n')
  estadocivil = input('Digite a letra correspondente ao seu estado civil: ')
  estadocivil = estadocivil.lower()
else: 
  print('Estado Civil Válido\n')