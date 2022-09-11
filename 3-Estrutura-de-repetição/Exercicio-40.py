print('DADOS SOBRE ACIDENTES DE TRÂNSITO')
codigo_cidade = int(input('Digite o número do código da cidade: '))
veiculos = int(input('Digite o número de veículos de passeio na cidade em 1999: '))
acidentes = int(input('Digite o número de acidentes de trânsito com vítima: '))
codigo_maior_acidente = codigo_cidade
maior_acidente = acidentes
codigo_menor_acidente = codigo_cidade
menor_acidente = acidentes
soma_veiculos = veiculos
soma_cidadesmenores = float(0)
contador_cidade = int(0)
if veiculos < 2000:
  soma_cidadesmenores = acidentes
  contador_cidade += 1
contador = int(1)
while contador < 5:
  codigo_cidade = int(input('\nDigite o número do código da cidade: '))
  veiculos = int(input('Digite o número de veículos de passeio na cidade em 1999: '))
  acidentes = int(input('Digite o número de acidentes de trânsito com vítima em 1999: '))
  if acidentes > maior_acidente:
    maior_acidente = acidentes
    codigo_maior_acidente = codigo_cidade
  elif acidentes < menor_acidente:
    menor_acidente = acidentes
    codigo_menor_acidente = codigo_cidade
  soma_veiculos += veiculos
  if veiculos < 2000:
    soma_cidadesmenores += acidentes
    contador_cidade += 1
  contador += 1
media_veiculos = soma_veiculos / 5
if soma_cidadesmenores != 0:
  media_cidadesmenores = soma_cidadesmenores / contador_cidade
else:
  media_cidadesmenores = float(0)
print(f'\n=== Maior índice de acidente de transito ===\nCidade código: {codigo_maior_acidente}\nÍndice: {maior_acidente}')
print(f'\n=== Menor índice de acidente de transito ===\nCidade código: {codigo_menor_acidente}\nÍndice: {menor_acidente}')
print(f'\n=== Média de veículos nas cidades juntas ===\nMédia: {media_veiculos}')
print(f'\n=== Média de acidentes de trânsito nas cidades com menos de 2.000 veículos ===\nMédia: {media_cidadesmenores}')