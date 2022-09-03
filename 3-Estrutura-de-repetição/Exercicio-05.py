print('CRESCIMENTO DE POPULAÇÃO DO PAÍS!')
população_a = int(input('Digite a população do País A: '))
while população_a == float:
  print('ERRO: A população deve ser um valor INTEIRO!\nTente Novamente')
  população_a = int(input('\nDigite a população do País A: '))
crescimento_a = float(input('Digite a taxa de crescimento do País A: ')) / 100

população_b = int(input('\nDigite a populção do País B: '))
while população_b == float or população_b <= população_a:
  print('ERRO: A população deve ser um número inteiro e ser maior que a população do País A\nTente Novamente')
  população_b = int(input('\nDigite a populção do País B: '))

crescimento_b = float(input('Digite a taxa de crescimento do País B: ')) / 100
while crescimento_b >= crescimento_a:
  print('ERRO: Taxa de crescimento do País B não pode ser maior ou igual a taxa do País A!\nTente Novamente')
  crescimento_b = float(input('\nDigite a taxa de crescimento do País B: ')) / 100

ano = int(0)
while população_a < população_b:
  população_a = int(população_a + (população_a * crescimento_a))
  população_b = int(população_b + (população_b * crescimento_b))
  ano = ano + 1
print(f'A população do País A vai precisar de {ano} anos para passar o País B')