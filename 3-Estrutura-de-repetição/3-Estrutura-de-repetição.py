# EXERCÍCIO 01
# print('NÚMERO ENTRE 0 E 10')
# numero = int(input('Digite uma nota entre 0 e 10: '))
# while numero > 10 or numero < 0:
#   print('\nValor Inválido!')
#   numero = int(input('Digite uma nota entre 0 e 10: '))


# EXERCÍCIO 02
# print('NOME DE USUÁRIO E SENHA')
# usuario = input('Digite um nome de usuário: ')
# senha = input('Digite uma senha: ')
# while usuario == senha:
#   print('\nERRO: Usuário e Senha não podem ser iguais!\nTente novamente\n')
#   usuario = input('Digite um nome de usuário: ')
#   senha = input('Digite uma senha: ')

# EXERCÍCIO 03
# print('VALIDAÇÃO DE INFORMAÇÕES')
# nome = input('Digite um nome: ')
# while len(nome) <= 3:
#   print('ERRO: O nome tem que ter mais de 3 caracteres!\nTente novamenteo\n')
#   nome = input('Digite um nome: ')
# else:
#   print('Nome Válido!\n')
# idade = int(input('Digite uma idade: '))

# while idade > 150 or idade < 0:
#   print('ERRO: A idade tem que ser entre 0 e 150\nTente Noamente\n')
#   idade = int(input('Digite uma idade: '))
# else:
#   print('Idade Válida!\n')

# salario = float(input('Digite o valor de um salário: '))
# while salario <= 0:
#   print('ERRO: O Salário tem que ser maior que 0\nTente Novamente\n')
#   salario = float(input('Digite o valor de um salário: '))
# else:
#   print('Salário Válido!\n')

# sexo = input('Digite [F] para Feminino ou [M] para Masculino: ')
# sexo = sexo.lower()
# while sexo != 'f' and sexo != 'm':
#   print('ERRO: Sexo Inválido!\nTente Novamente\n')
#   sexo = input('Digite [F] para Feminino ou [M] para Masculino: ')
#   sexo = sexo.lower()
# else:
#   print('Sexo Válido!\n')

# print('Estado Civil\n[S]- Solteiro(a)\n[C]- Casado(a)\n[V]- Viúvo(a)\n[D]- Divorciado(a)')
# estadocivil = input('Digite a letra correspondente ao seu estado civil: ')
# estadocivil = estadocivil.lower()
# while estadocivil != 's' and estadocivil != 'c' and estadocivil != 'v' and estadocivil != 'd':
#   print('ERRO: Estado Civil Inválido\nTente novamente\n')
#   estadocivil = input('Digite a letra correspondente ao seu estado civil: ')
#   estadocivil = estadocivil.lower()
# else: 
#   print('Estado Civil Válido\n')

# EXERCÍCIO 04
# print('CRESCIMENTO DE POPULAÇÃO DO PAÍS!')
# população_a = int(80000)
# população_b = int(200000)
# crescimento_a = 3 / 100
# crescimento_b = 1.5 / 100
# ano = int(0)
# while população_a < população_b:
#   população_a = int(população_a + (população_a * crescimento_a))
#   população_b = int(população_b + (população_b * crescimento_b))
#   ano = ano + 1
#   print(população_a, população_b)
# print(f'A população do País A vai precisar de {ano} anos')


# EXERCÍCIO 05
# print('CRESCIMENTO DE POPULAÇÃO DO PAÍS!')
# população_a = int(input('Digite a população do País A: '))
# while população_a == float:
#   print('ERRO: A população deve ser um valor INTEIRO!\nTente Novamente')
#   população_a = int(input('\nDigite a população do País A: '))
# crescimento_a = float(input('Digite a taxa de crescimento do País A: ')) / 100

# população_b = int(input('\nDigite a populção do País B: '))
# while população_b == float or população_b <= população_a:
#   print('ERRO: A população deve ser um número inteiro e ser maior que a população do País A\nTente Novamente')
#   população_b = int(input('\nDigite a populção do País B: '))

# crescimento_b = float(input('Digite a taxa de crescimento do País B: ')) / 100
# while crescimento_b >= crescimento_a:
#   print('ERRO: Taxa de crescimento do País B não pode ser maior ou igual a taxa do País A!\nTente Novamente')
#   crescimento_b = float(input('\nDigite a taxa de crescimento do País B: ')) / 100

# ano = int(0)
# while população_a < população_b:
#   população_a = int(população_a + (população_a * crescimento_a))
#   população_b = int(população_b + (população_b * crescimento_b))
#   ano = ano + 1
# print(f'A população do País A vai precisar de {ano} anos para passar o País B')

# EXERCÍCIO 06
# numero = 1
# listanumero = []
# while numero <= 20:
#   print(numero)
#   listanumero.append(numero)
#   numero = numero + 1
# print(listanumero)

# EXERCÍCIO 07
# numero1 = float(input('Digite o 1º numero: '))
# numero2 = float(input('Digite o 2º numero: '))
# numero3 = float(input('Digite o 3º número: '))
# numero4 = float(input('Digite o 4º número: '))
# numero5 = float(input('Digite o 5º número: '))
# listanumero = [numero1, numero2, numero3, numero4, numero5]
# maior = numero1
# for numero in listanumero:
#   if numero > maior:
#     maior = numero
# print(f'O maior número é: {maior}')


# EXERCÍCIO 08
# numero1 = float(input('Digite o 1º numero: '))
# numero2 = float(input('Digite o 2º numero: '))
# numero3 = float(input('Digite o 3º número: '))
# numero4 = float(input('Digite o 4º número: '))
# numero5 = float(input('Digite o 5º número: '))
# listanumero = [numero1, numero2, numero3, numero4, numero5]
# soma = 0
# for numero in listanumero:
#   soma = soma + numero 
# else:
#   media = soma / 5
#   print(f'A soma dos número é: {soma}\nA média dos números é: {media}')


# EXERCÍCIO 09
# numero = int(1)
# while numero <= 50:
#   par = numero % 2
#   if par != 0:
#     print(numero)
#   numero = numero + 1

# EXERCÍCIO 10
# numero1 = int(input('Digite o 1º número: '))
# numero2 = int(input('Digtie o 2º número: '))
# if numero1 > numero2:
#   maior = numero1
#   menor = numero2
# elif numero2 > numero1:
#   maior = numero2
#   menor = numero1
# if numero1 == numero2:
#   print('Os 2 números são iguais!')
# elif menor + 1 != maior:
#   menor = menor + 1
#   while menor < maior:
#     print(menor)
#     menor = menor + 1
# else:
#   print('Não tem números inteiros entre eles!')


# EXERCÍCIO 11

# EXERCÍCIO 12

# EXERCÍCIO 13

# EXERCÍCIO 14

# EXERCÍCIO 15

# EXERCÍCIO 16

# EXERCÍCIO 17

# EXERCÍCIO 18

# EXERCÍCIO 19

# EXERCÍCIO 20