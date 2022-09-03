# EXERCÍCIO 01
# print('O MAIOR NÚMERO')
# numero1 = float(input('Digite um número: '))
# numero2 = float(input('Digite outro número: '))
# if numero1 > numero2:
#   print(f'\nO maior número é: {numero1}')
# elif numero1 == numero2:
#   print('\nAmbos os números são iguais!')
# else:
#   print(f'\nO maior número é: {numero2}')


# EXERCÍCIO 02
# print('VALOR POSITIVO OU NEGATIVO')
# numero = float(input('Digite um valor: '))
# if numero > 0:
#   print('O valor é positivo!')
# elif numero < 0:
#   print('O valor é negativo!')
# else:
#   print('Valor igual a zero')

# EXERCÍCIO 03
# print('F OU M')
# letra = input("Digite 'F' para Feminino ou 'M' para Masculino: ")
# if letra == 'f' or letra == 'F':
#   print('Sexo Feminino')
# elif letra == 'm' or letra == 'M':
#   print('Sexo Masculino')
# else:
#   print('Sexo inválido')


# EXERCÍCIO 04
# print('VOGAL OU CONSOANTE')
# letra = input('Digite uma letra: ')
# letra = letra.lower()
# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#   print('Vogal!')
# else:
#   print('Consoante!')

# # EXERCÍCIO 05
# print('NOTA DO ALUNO')
# nota1 = float(input('Digite a primeira nota do aluno: '))
# nota2 = float(input('Digite a segunda nota do aluno: '))
# media = float((nota1 + nota2) / 2)
# if media == 10:
#   print('Aluno APROVADO COM DISTINÇÃO')
# elif media >= 7:
#   print('Aluno APROVADO')
# else:
#   print('Aluno REPROVADO')


# EXERCÍCIO 06
# print('O MAIOR DE 3 NÚMEROS')
# numero1 = float(input('Digite o 1ª número: '))
# numero2 = float(input('Digite o 2ª número: '))
# numero3 = float(input('Digite o 3º número: '))
# maior = float(0)
# if numero1 > maior or numero1 < 0:
#   maior = numero1
# if numero2 > maior:
#   maior = numero2
# if numero3 > maior:
#   maior = numero3
# print(f'\nO maior número é: {maior}')

# EXERCÍCIO 07
# print('O MAIOR E O MENOR DE 3 NÚMEROS')
# numero1 = float(input('Digite o 1ª número: '))
# numero2 = float(input('Digite o 2ª número: '))
# numero3 = float(input('Digite o 3º número: '))
# maior = float(0)
# menor = float(0)
# if numero1 > maior or numero1 < 0:
#   maior = numero1
# if numero2 > maior:
#   maior = numero2
#   menor = numero1
# elif numero2 < numero1:
#   menor = numero2
# if numero3 > maior:
#   maior = numero3
# elif numero3 < menor:
#   menor = numero3
# print(f'\nO MAIOR número é: {maior}')
# print(f'O MENOR número é {menor}')

# EXERCÍCIO 08
# print('PRODUTO MAIS BARATO')
# produto1 = float(input('Digite o valor do 1º produto: R$'))
# produto2 = float(input('Digite o valor do 2º produto: R$'))
# produto3 = float(input('Digite o valor do 3º produto: R$'))
# if produto1 < produto2 and produto1 < produto3:
#   print(f'O produto mais barato é o 1º Produto, pelo preço de R${produto1}')
# elif produto2 < produto1 and produto2 < produto3:
#   print(f'O produto mais barato é o 2º Produto, pelo preço de R${produto2}')
# else:
#   print(f'O produto mais barato é o 3º Produto, pelo preço de R${produto3}')



# EXERCÍCIO 09
# print('ORDEM DECRESCENTE')
# numero1 = float(input('Digite um número: '))
# numero2 = float(input('Digite outro número: '))
# numero3 = float(input('Digite outro número: '))
# # Se número 1 e número 2 forem iguais
# if numero1 == numero2:
#   if numero1 > numero3:
#     primeiro = numero1
#     segundo = numero2
#     terceiro = numero3
#   if numero1 == numero3:
#     primeiro = numero1
#     segundo = numero2
#     terceiro = numero3
#   if numero1 < numero3:
#     primeiro = numero3
#     segundo = numero1
#     terceiro = numero2
# # Se número 1 e número 3 forem iguais
# elif numero1 == numero3:
#   if numero1 > numero2:
#     primeiro = numero1
#     segundo = numero3
#     terceiro = numero2
#   if numero1 == numero2:
#     primeiro = numero1
#     segundo = numero2
#     terceiro = numero3
#   if numero1 < numero2:
#     primeiro = numero2
#     segundo = numero1
#     terceiro = numero3
# # SE TODOS OS NÚMEROS FOREM IGUAIS
# elif numero2 == numero3:
#   if numero2 > numero1:
#     primeiro = numero2
#     segundo = numero3
#     terceiro = numero1
#   if numero2 == numero1:
#     primeiro == numero1
#     segundo == numero2
#     terceiro == numero3
#   if numero2 < numero1:
#     primeiro = numero1
#     segundo = numero2
#     terceiro = numero3
# elif numero1 == numero2 and numero1 == numero3:
#   primeiro = numero1
#   segundo = numero2
#   terceiro = numero3
# # SE NENHUM NÚMERO FOR IGUAL
# else:
#   primeiro = numero1
#   if numero2 > primeiro and numero2 > numero3:
#     primeiro = numero2
#     if numero1 < numero3:
#       terceiro = numero1
#       segundo = numero3
#     else:
#       terceiro = numero3
#       segundo = numero1
# # SE NÚMERO 2 FOR O MAIOR 
#   elif numero3 > primeiro and numero3 > numero2:
#     primeiro = numero3
#     if numero2 < numero1:
#       terceiro = numero2
#       segundo = numero1
#     else: 
#       terceiro = numero1
#       segundo = numero2
# # SE NÚMERO 3 FOR O MAIOR
#   elif numero2 < numero3:
#     terceiro = numero2
#     segundo = numero3
#   else: 
#     terceiro = numero3
#     segundo = numero2
# # SE NÚMERO 1 FOR O MAIOR
# print(f'O 1º número é: {primeiro}\nO 2º número é: {segundo}\nO 3º número é: {terceiro}')





# EXERCÍCIO 10
# print('TURNO QUE VOCÊ ESTUDA')
# print('Qual turno você estuda:\nM- Matutino\nV- Vespertino\nN- Noturno')
# turno = input('Digite a letra correspondente ao seu turno: ')
# turno = turno.lower()
# if turno == 'm':
#   print('Bom Dia!')
# elif turno == 'v':
#   print('Boa Tarde!')
# elif turno == 'n':
#   print('Boa Noite!')
# else:
#   print('Valor Inválido!')


# EXERCÍCIO 11
# print('AUMENTO DE SALÁRIO')
# salario = float(input('Digite o valor do salário: '))
# if salario <= 280:
#   percentual = 20
#   valoraumento = float(salario * 20 / 100)
#   novosalario = float(salario + valoraumento)
# elif salario > 280 and salario < 700:
#   percentual = 15
#   valoraumento = float(salario * 15 /100)
#   novosalario = float(salario + valoraumento)
# elif salario >= 700 and salario < 1500:
#   percentual = 10
#   valoraumento = float(salario * 10 /100)
#   novosalario = float(salario + valoraumento)
# elif salario >= 1500:
#   percentual = 5
#   valoraumento = float(salario * 5 /100)
#   novosalario = float(salario + valoraumento)
# print(f'\nO salário antes do reajuste era: R${salario}')
# print(f'O percentual de aumento aplicado foi de: {percentual}%')
# print(f'O valor do aumento foi de: R${valoraumento}')
# print(f'O novo salário é de: R${novosalario}')


# EXERCÍCIO 12
# print('FOLHA DE PAGAMENTO')
# valorhora = float(input('Digite o valor da sua hora de trabalho: R$'))
# horastrabalho = float(input('Digite a quantidade de horas trabalhadas no mês: '))
# salariobruto = float(valorhora * horastrabalho)
# if salariobruto <= 900:
#   percentual = 0
#   ir = float(0)
# elif salariobruto <= 1500:
#   percentual = 5
#   ir = float(salariobruto * 5 /100)
# elif salariobruto <= 2500:
#   percentual = 10
#   ir = float(salariobruto * 10 /100)
# elif salariobruto > 2500:
#   percentual = 20
#   ir = float(salariobruto * 20 /100)
# sindicato = float(salariobruto * 3 /100)
# fgts = float(salariobruto * 11 /100)
# descontos = ir + sindicato
# salarioliquido = salariobruto - descontos
# print(f'\nSalário Bruto: R${salariobruto}')
# print(f'\nDesconto do IR ({percentual}%): R${ir}\nDesconto do Sindicato (3%): R${sindicato}')
# print(f'Valor do FGTS (11%): R${fgts}')
# print(f'Total de descontos: R${descontos}')
# print(f'\nSalário Líquido: R${salarioliquido}')


# EXERCÍCIO 13
# print('DIA DA SEMANA')
# numero = float(input('Digite um número: '))
# if numero == 1:
#   dia = 'Domingo'
# elif numero == 2:
#   dia = 'Segunda-Feira'
# elif numero == 3:
#   dia = 'Terça-Feira'
# elif numero == 4:
#   dia = 'Quarta-Feira'
# elif numero == 5:
#   dia = 'Quinta-Feira'
# elif numero == 6:
#   dia = 'Sexta-Feira'
# elif numero == 7:
#   dia = 'Sábado'
# else: 
#   dia = 'Valor Inválido!'
# print(dia)

# EXERCÍCIO 14
# print('NOTAS DO SEMESTRE')
# nota1 = float(input('Digite a 1º nota do aluno: '))
# nota2 = float(input('Digite a 2º nota do aluno: '))
# media = (nota1 + nota2) / 2
# if media >= 9 and media <=10:
#   conceito = 'A'
#   mensagem = 'APROVADO'
# elif media >= 7.5 and media < 9:
#   conceito = 'B'
#   mensagem = 'APROVADO'
# elif media >= 6 and media < 7.5:
#   conceito = 'C'
#   mensagem = 'APROVADO'
# elif media >= 4 and media < 6:
#   conceito = 'D'
#   mensagem = 'REPROVADO'
# elif media < 4:
#   conceito = 'E'
#   mensagem = 'REPROVADO'
# print(f'\nA 1º nota foi: {nota1}\nA 2ª nota foi: {nota2}')
# print(f'A média das notas foi: {media}\nVocê ficou com {conceito} e está {mensagem}')


# EXERCÍCIO 15
# print('TRIÂNGULO')
# lado1 = float(input('Digite o tamanho do 1º lado do triângulo: '))
# lado2 = float(input('Digite o tamano do 2º lado do triângulo: '))
# lado3 = float(input('Digite o tamanaho do 3º lado do triângulo: '))
# if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
#   print('\nOs tamanhos PODEM formar um trinângulo')
#   if lado1 == lado2 and lado1 == lado3:
#     print('O triângulo é Equilátero!')
#   elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#     print('O triângulo é Isósceles!')
#   else: 
#     print('O triângulo é Escaleno')
# else:
#   print('\nOs tamanhos NÃO PODEM formar um triângulo')


# EXERCÍCIO 16
# print('QUANTIDADE DE RAIZ DA EQUAÇÃO DO 2º GRAU')
# a = float(input("Informe o valor de 'a': "))
# if a == 0:
#   print('\nA equação não é do 2º grau!')
# else:
#   b = float(input("Informe o valor de 'b': "))
#   c = float(input("Informe o valor de 'c': "))
#   delta = (b ** 2) - (4 * a * c)
#   if delta < 0:
#     print('\nA equação não possui raizes reais!')
#   elif delta == 0:
#     print('\nA equação possui apenas uma raiz real!')
#   else: 
#     print('\n1A equação possui 2 raizes reais!')


# EXERCÍCIO 17
# print('ANO BISSEXTO')
# ano = int(input('Digite o número de um ano: '))
# bissexto = ano % 4
# if bissexto == 0:
#   print(f'O ano {ano} é BISSEXTO!')
# else: 
#   print(f'O ano {ano} NÃO É BISSEXTO!')


# EXERCÍCIO 18
# print('VALIDAÇÃO DE DATA')
# dia = int(input("Digite uma data no formato 'dd/mm/aaaa':\ndd: "))
# mes = int(input('mm: '))
# ano = int(input('aaaa: '))
# bissexto = ano % 4
# if ano <= 0 or mes <= 0 or mes > 12 or dia > 31 or dia <= 0:
#   print('DATA INVÁLIDA!')
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
#   print('DATA INVÁLIDA!')
# elif bissexto == 0 and mes == 2 and dia > 29:
#   print('DATA INVÁLIDA!')
# elif bissexto != 0 and mes == 2 and dia > 28:
#   print('DATA INVÁLIDA!')
# else:
#   print('DATA VÁLIDA!')


# EXERCÍCIO 19
# print('LEITURA DE NÚMEROS')
# numero = int(input('Digite um número inteiro menor que 1000: '))
# if numero == 0:
#   print('Zero é um número nulo')
# elif numero == 1:
#   print('1 unidade')
# elif numero < 10:
#   numero = str(numero)
#   lista = [numero]
#   unidade = lista[0]
#   print(f'{unidade} unidades')
# elif numero >= 10 and numero < 100:
#   numero = str(numero)
#   lista = [numero[0], numero[1]]
#   dezena = lista[0]
#   unidade = lista[1]
#   if unidade == '0' and dezena != '1':
#     print(f'{dezena} dezenas')
#   elif unidade == '0' and dezena == '1':
#     print(f'{dezena} dezena')
#   elif unidade == '1' and dezena == '1':
#     print(f'{dezena} dezena e {unidade} unidade')
#   elif unidade == '1':
#     print(f'{dezena} dezenas e {unidade} unidade') 
#   elif dezena == '1':
#     print(f'{dezena} dezena e {unidade} unidades')  
#   else:
#     print(f'{dezena} dezenas e {unidade} unidades')
# elif numero > 99 and numero < 1000:
#   numero = str(numero)
#   lista = [numero[0], numero[1], numero[2]]
#   centena = lista[0]
#   dezena = lista[1]
#   unidade = lista[2]
#   if centena == '1' and dezena == '1' and unidade == '1':
#     print('1 centena, 1 dezena e 1 unidade')
#   elif centena == '1' and dezena == '1':
#     if unidade == '0':
#       print(f'{centena} centena e {dezena} dezena')
#     else:
#       print(f'{centena} centena, {dezena} dezena e {unidade} unidades')
#   elif centena == '1' and unidade == '1':
#     if dezena == '0':
#       print(f'{centena} centena e {unidade} unidade')
#     else:
#       print(f'{centena} centena, {dezena} dezenas e {unidade} unidade')
#   elif dezena == '1' and unidade == '1':
#     print(f'{centena} centanas, {dezena} dezena e {unidade} unidade')
#   elif dezena == '0' and unidade == '0':
#     if centena == '1':
#       print(f'{centena} centena')
#     else:
#       print(f'{centena} centenas')
#   elif dezena == '0':
#     if unidade == '1' and centena != '1':
#       print(f'{centena} centenas e {unidade} unidade')
#     elif centena == '1':
#       print(f'{centena} centena e {unidade} unidades')
#     else:
#       print(f'{centena} centenas e {unidade} unidades')
#   elif unidade == '0':
#     if dezena == '1':
#       print(f'{centena} centenas e {dezena} dezena')
#     else:
#       print(f'{centena} centanas e {dezena} dezenas')
#   elif dezena == '1':
#     print(f'{centena} centenas, {dezena} denzena e {unidade} unidades')
#   elif unidade == '1':
#     print(f'{centena} centenas, {dezena} denzenas e {unidade} unidade')
#   elif centena == '1':
#     print(f'{centena} centena, {dezena} denzenas e {unidade} unidades')
#   else:
#     print(f'{centena} centenas, {dezena} dezenas e {unidade} unidades')


# EXERCÍCIO 20
# print('APROVADO OU REPROVADO V2')
# nota1 = float(input('Digite a 1ª nota do aluno: '))
# nota2 = float(input('Digte a 2ª nota do aluno: '))
# nota3 = float(input('Digite a 3ª nota do aluno: '))
# media = (nota1 + nota2 + nota3) / 3
# if media == 10:
#   print('\nAprovado com Distinção')
# elif media >= 7:
#   print(f'\nAPROVADO\nSua média foi: {media:.2f}')
# else:
#   print(f'\nREPROVADO\nSua média foi: {media:.2f}')



# EXERCÍCIO 21
# print('CAIXA ELETRÔNICO')
# saque = int(input('Digite o valor que você deseja sacar: '))
# while saque < 10 or saque > 600:
#   print('VALOR NÃO PERMITIDO\nMínimo R$10\nMáximo R$600')
#   saque = int(input('\nDigte outro valor para saque: '))
# def fnota50(resto):
#   nota50 = resto // 50
#   print(f'{nota50} de R$50')
# def fnota10(resto):
#   nota10 = resto // 10
#   print(f'{nota10} de R$10')
# def fnota5(resto):
#   nota5 = resto // 5
#   print(f'{nota5} de R$5')
# def fnota1(resto):
#   nota1 = resto // 1
#   print(f'{nota1} de R$1')
# if saque >= 100:
#   print('Você vai receber notas de:')
#   nota100 = saque // 100
#   resto = saque % 100
#   print(f'{nota100} de R$100')
#   if resto >= 50:
#     fnota50(resto)
#     resto = resto % 50
#   if resto >= 10:
#     fnota10(resto)
#     resto = resto % 10
#   if resto >= 5:
#     fnota5(resto)
#     resto = resto % 5
#   if resto >= 1:
#     fnota1(resto)
#     resto = resto % 1
# elif saque >= 50:
#   print('Você vai receber notas de:')
#   nota50 = saque // 50
#   resto = saque % 50
#   print(f'{nota50} de R$50')
#   if resto >= 10:
#     fnota10(resto)
#     resto = resto % 10
#   if resto >= 5:
#     fnota5(resto)
#     resto = resto % 5
#   if resto >= 1:
#     fnota1(resto)
#     resto = resto % 1
# elif saque >= 10:
#   print('Você vai receber notas de:')
#   nota10 = saque // 10
#   resto = saque % 10
#   print(f'{nota10} de R$10')
#   if resto >= 5:
#     fnota5(resto)
#     resto = resto % 5
#   if resto >= 1:
#     fnota1(resto)
#     resto = resto % 1

# EXERCÍCIO 22
# print('PAR OU IMPAR')
# numero = int(input('Digite um número: '))
# par = numero % 2
# if par == 0:
#   print('Número PAR')
# else:
#   print('Número IMPAR')

# EXERCÍCIO 23
# print('NÚMERO INTEIRO OU DECIMAL')
# numero = float(input('Digite um número: '))
# resto = numero % 1
# if resto == 0.0:
#   print('Número INTEIRO')
# else:
#   print('Número DECIMAL')


# EXERCÍCIO 24
# print('OPERAÇÕES DE 2 NÚMEROS')
# numero1 = float(input('Digite um número: '))
# numero2 = float(input('Digite outro número: '))
# print('OPERAÇÕES:\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão')
# operação = int(input('Digite o número correspondente a operação que você deseja realizar: '))
# if operação == 1:
#   resultado = numero1 + numero2
# elif operação == 2:
#   resultado = numero1 - numero2
# elif operação == 3:
#   resultado = numero1 * numero2
# elif operação == 4:
#   resultado = numero1 / numero2
# print(f'O resultado é: {resultado:.2f}')
# par = resultado % 2
# resto = resultado % 1
# if par == 0:
#   print('\nO resultado é PAR')
# elif par != 0 and resto != 0.0:
#   print('\nO resultado NÃO É PAR NEM IMPAR, por ser decimal')
# else: 
#   print('\nO resultado é IMPAR')
# if resultado == 0:
#   print('O número é NULO')
# elif resultado > 0:
#   print('O resultado é POSITIVO')
# else:
#   print('O resultado é NEGATIVO')
# if resto == 0.0:
#   print('O resultado é INTEIRO')
# else: 
#   print('O resultado é DECIMAL')

# EXERCÍCIO 25
# print('INVESTIGAÇÃO CRIMINAL')
# pergunta1 = int(input('[1]SIM [2]NÃO\nVocê telefonou para a vitma? '))
# afirmação = 0
# if pergunta1 == 1:
#   afirmação = afirmação + 1
# pergunta2 = int(input('Você esteve no local do crime? '))
# if pergunta2 == 1:
#   afirmação = afirmação + 1
# pergunta3 = int(input('Você mora perto da vítima? '))
# if pergunta3 == 1:
#   afirmação = afirmação + 1
# pergunta4 = int(input('Você devia para a vítima? '))
# if pergunta4 == 1:
#   afirmação = afirmação + 1
# pergunta5 = int(input('Você já trabalhou com a vítima? '))
# if pergunta5 == 1:
#   afirmação = afirmação + 1
# if afirmação == 2:
#   print('Você é SUSPEITO')
# elif afirmação == 3 or afirmação == 4:
#   print('Você é CÚMPLICE')
# elif afirmação == 5:
#   print('Você é o ASSASSINO')
# else:
#   print('Você é INOCENTE')

# EXERCÍCIO 26
# print('VENDA DE COMBUSTÍVEL')
# litro = float(input('Digite quantos litros de comustível você deseja: '))
# print('\nQUAL COMBUSTÍVEL VOCÊ DESEJA?\n[A]- Álcool\n[G]- Gasolina\n')
# combustivel = input('Digite a letra correspondente ao combustível que deseja: ')
# combustivel = combustivel.lower()
# if combustivel == 'a':
#   if litro <= 20:
#     preco = 1.90 * litro
#     total = preco - (preco * 3 / 100)
#     print(f'O total a ser pago é de: R${total}')
#   else:
#     preco = 1.90 * litro
#     total = preco - (preco * 5 / 100)
#     print(f'O total a ser pago é de: R${total}')
# elif combustivel == 'g':
#   if litro <= 20:
#     preco = 2.50 * litro
#     total = preco - (preco * 4 / 100)
#     print(f'O total a ser pago é de: R${total}')
#   else:
#     preco = 2.50 * litro
#     total = preco - (preco * 6 / 100)
#     print(f'O total a ser pago é de: R${total}')
# else:
#   print('Erro ao selecionar combustível, reinicie o programa')


# EXERCÍCIO 27
# print('COMPRAS DE FRUTAS')
# kgmorango = float(input('MORANGO\nDigite quantos Kg de Morango você deseja: '))
# kgmaca = float(input('\nMAÇA\nDigite quantos Kg de maça você deseja comprar: '))
# if kgmorango <= 5:
#   valormorango = 2.50 * kgmorango
# else: 
#   valormorango = 2.20 * kgmorango
# if kgmaca <= 5:
#   valormaca = 1.80 * kgmaca
# else:
#   valormaca = 1.50 * kgmaca
# totalkg = kgmaca + kgmorango
# valortotal = valormorango + valormaca
# if totalkg > 8 or valortotal > 25:
#   valortotal = valortotal - (valortotal * 10 / 100)
# print(f'\nO total a se pagar é de: R${valortotal:.2f}')

# EXERCÍCIO 28
# print('PROMOÇÃO DE CARNES')
# print('\nESCOLHA UM TIPO DE CARNE:\n[1] - File Duplo\n[2] - Alcatra\n[3] - Picanha')
# carne = int(input('Digite o número correspondente a carne que você deseja: '))
# kg = float(input('Digite quantos Kg de carne você deseja: '))
# if carne == 1:
#   tipocarne = 'File Duplo'
#   if kg <= 5:
#     preco = 4.90 * kg
#   else:
#     preco = 5.80 * kg
# elif carne == 2:
#   tipocarne = 'Alcatra'
#   if kg <= 5:
#     preco = 5.90 * kg
#   else:
#     preco = 6.80 * kg
# elif carne == 3:
#   tipocarne = 'Picanha'
#   if kg <=5 :
#     preco = 6.90 * kg
#   else:
#     preco = 7.80 * kg
# print('Deseja utilizar o cartão Tabajara? \n[1] SIM OU [2] NÃO')
# cartao = int(input('Digite o número correspondente a sua escolha: '))
# if cartao == 1:
#   desconto = preco * 5 / 100
#   precopagar = preco - desconto
#   tipopagamento = 'COM CARTÃO TABAJARA'
# else: 
#   tipopagamento = 'SEM CARTÃO TABAJARA'
#   desconto = int(0)
#   precopagar = preco
# print(f'\nCUPOM FISCAL\nTIPO DE CARNE: {tipocarne}\nQUANTIDADE DE CARNE: {kg}Kg\nPREÇO TOTAL: R${preco:.2f}\nTIPO DE PAGAMENTO: {tipopagamento}\nVALOR DO DESCONTO: R${desconto:.2f}\nVALOR A PAGAR: R${precopagar:.2f}')