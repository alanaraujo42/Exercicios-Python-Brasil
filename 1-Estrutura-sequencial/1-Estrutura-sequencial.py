# EXERCÍCIO 1
# print('Olá Mundo')

# EXERCÍCIO 2
# n = input('Digite um número: ')
# print(f'O número informado foi {n}')

# EXERCÍCIO 3
# n1 = float(input('Digite um número: '))
# n2 = float(input('Digite outro número: '))
# print(f'A soma entre eles é {int(n1 + n2)}')

# EXERCÍCIO 4
# print('AS NOTAS BIMESTRAIS')
# nota_1 = float(input('1º Nota: '))
# nota_2 = float(input('2º Nota: '))
# nota_3 = float(input('3º Nota: '))
# nota_4 = float(input('4º Nota: '))
# media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
# print(f'A média das notas é: {media}')

#EXERCÍCIO 5
# metro = float(input('Digite um tamanho em metros: '))
# centimentro = metro * 100
# print(f'O valor em centimetros é {centimentro}cm')


# EXERCÍCIO 6
# raio = float(input('Digite o raio do círculo: '))
# area = float(3.1415 * (raio ** 2))
# print(f'A área do círculo é: {area}')

# EXERCÍCIO 7
# print('DOBRO DA ÁREA DO QUADRADO')
# lado = float(input('Digite o tamanho do lado do quadradro: '))
# area = float(lado ** 2)
# print(f'A área do quadrado é {area}cm² e o seu dobro é {area * 2}cm²')


# EXERCÍCIO 8
# print('SALÁRIO DO MÊS COM BASE EM HORAS TRABALHADAS')
# valor_hora = float(input('Digite o valor que você ganha por hora: R$'))
# horas_trabalho = int(input('Digite quantas horas você trabalha no mês: '))
# salario = valor_hora * horas_trabalho
# print(f'Seu salário é: R${salario}')

# EXERCÍCIO 9
# print('GRAUS FAHRENHEIT PARA GRAUS CELSIUS')
# fah = float(input('Digite a temperatura em Fahrenheit: '))
# celsius = float(5 * ((fah - 32) / 9))
# print(f'A temperatura em Celsius é: {celsius}°C')

# EXERCÍCIO 10
# print('GRAUS CELSIUS PAR GRAUS FAHRENHEIT')
# celsius = float(input('Digite a temperaura em Celsius: '))
# fah = float(((celsius * 9 / 5) + 32))
# print(f'A temperatura em Fahrenheit é: {fah}°F')

# EXERCÍCIO 11
# print('NÚMEROS INTEIROS E NÚMEROS REAIS')
# n1 = int(input('Digite um número Inteiro: '))
# n2 = int(input('Digite outro número Inteiro: '))
# n3 = float(input('Digite um número Real: '))
# resultado1 = ((n1 * 2) * (n2 / 2))
# resultado2 = ((n1 * 3) + n3)
# resultado3 = (n3 ** 3)
# print(f'O produto do dobro do primeiro com metade do segundo é {resultado1}')
# print(f'A soma do triplo do primeiro com o terceiro é {resultado2}')
# print(f'O terceiro elevado ao cubo é {resultado3}')

# EXERCÍCIO 12
# print('SEU PESO IDEAL')
# altura = float(input('Digite a sua altura: '))
# pideal = float((72.7 * altura) - 58)
# print(f'Seu peso ideal é: {pideal}')

# EXERCÍCIO 13
# print('PESO IDEAL PARA HOMENES E MULHERES')
# altura = float(input('Digite a sua altura: '))
# pideal_h = float((72.7 * altura) - 58)
# pideal_m = float((62.1 * altura) - 44.7)
# sexo = input("Digite 'M' para Masculino ou 'F' para Feminino: ")
# if sexo == 'M':
#   print(f'O peso ideal para homens é: {pideal_h:.2f}')
# else:
#   print(f'O peso ideal para mulheres é: {pideal_m:.2f}')

# EXERCÍCIO 14
# print('REGULAMENTO DE PESCA')
# peso = float(input('Digite o peso do peixe: '))
# excesso = float(peso - 50)
# multa = float(excesso * 4)
# if excesso < 1:
#   print(f'O peso do peixe é de {peso}Kg, não excedeu o limite permitido de 50Kg \nNão há necessidade de pagar multa')
# else:
#   print(f'O peso do peixe é de {peso} e ele excedeu o limite permitido de 50Kg')
#   print(f'O excesso é de {excesso:.2f}Kg e o valor da multa é de: R${multa:.2f}')


# EXERCÍCIO 15
# print('SALÁRIO E VALORES DESCCONTADOS')
# valorhora = float(input('Digite o valor que você ganha por hora: R$'))
# trabalhohora = float(input('Digite a quantidade de horas trabalhadas por mês: '))
# salariobruto = float(valorhora * trabalhohora)
# ir = float((salariobruto * 11) / 100)
# inss = float((salariobruto * 8) / 100)
# sindicato = float((salariobruto * 5) / 100)
# descontos = float(ir + inss + sindicato)
# salarioliquido = float(salariobruto - descontos)
# print(f'O seu Salário Bruto é R${salariobruto:.2f}')
# print(f'O valor que você paga para o INSS é de: R${inss:.2f}')
# print(f'O valor que você paga para o Sindicato é de: R${sindicato:.2f}')
# print(f'O seu Salário Liquido é de: R${salarioliquido:.2f}')


# EXERCÍCIO 16
# print('LOJA DE TINTAS')
# area = float(input('Qual o tamanho da área a ser pintada em m²: '))
# litro = float(area / 3)
# lata = int(litro / 18)
# if lata < 1:
#   valorlata = float(80)
#   lata = int(1)
# else:
#   valorlata = float(lata * 80)
# print(f'\nA quantidade de latas de tinta que você precisa é de: {lata} lata')
# print(f'O valor total é de: R${valorlata} \nVolte Sempre!!')

# EXERCÍCIO 17
# print('LOJA DE TINTAS 2.0')
# area = float(input('Qual o tamanho da área a ser pintada em m²: '))
# litro = float(area / 6)
# lata = int(litro / 18)
# galao = int(litro / 3.6)
# if lata < 1:
#   valorlata = float(80)
#   lata = int(1)
# else:
#   valorlata = float(lata * 80)
# if galao < 1:
#   valorgalao = float(25)
#   galao = int(1)
# else:
#   valorgalao = float(galao * 25)
# print('OPÇÕES DE COMPRA:')
# print(f'1ª Opção: Somente {lata} lata(s) de tintas de 18L, sendo o valor total: R${valorlata}')
# print(f'2ª Opção: Somente {galao} galão(ões)) de tinta de 3,6L, sendo o valor total: R${valorgalao}')
# litrofolga = float(litro + ((litro * 10) / 100))
# if litrofolga <= 3.6:
#   lata = int(0) 
#   galao = int(1)
# else:
#   lata = int(0)
#   galao = int(0)
#   while (litrofolga > 3.6):
#     galao = int(galao + 1)
#     litrofolga = float(litrofolga - 3.6)
#     if galao == 5:
#       galao = int(0)
#       lata = int(lata + 1)
# valorgalao = float(galao * 25)
# valorlata = float(lata * 80)
# print(f'3º Opção: {lata} lata(s) de tinta de 18L e {galao} galão(ões) de tinta de 3,6L\nSendo o valor total: R${valorlata} da lata(s) e R${valorgalao} do galão(ões)')

# EXERCÍCIO 18
# print('TEMPO PARA DOWNLOAD')
# arquivo = float(input('Informe o tamanho do arquivo para download em MB: '))
# velocidade = float(input('Informe a velocidade da internet em Mbps: '))
# velocidadereal = float(velocidade / 8)
# minutos = float( (arquivo / velocidadereal) / 60)
# print(f'O tempo aproximado para o download do arquivo é de: {minutos:.1f} minutos')

# HOJE 22/08/2022 FOI O DIA QUE EU TERMINEI DE FAZER OS EXERCÍCIOS SEQUENCIAL DA PYTHON BRASIL, COMECEI NO DIA 17/08/22, APESAR DE NÃO TER FEITO TODOS OS DIAS, MAS LEVOU EM MÉDIA UNS 5-6 DIAS PARA COMPLETAR