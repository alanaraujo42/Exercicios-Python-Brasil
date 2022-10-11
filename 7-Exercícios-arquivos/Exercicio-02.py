nomes = []
dados = []
dados_convertido = []
porcentagem = []

def conversao(item):
  resultado = item / 1048576
  dados_convertido.append(resultado)

def percentual(item, total):
  resultado = (item * 100) / total
  porcentagem.append(resultado)

total = float(0)
with open ('7-exercícios-arquivos/usuarios.txt', 'r') as arquivo:
  for linha in arquivo:
    linha = linha.strip()
    nome = linha[:15]
    dado = int(linha[16:])
    total += dado
    nomes.append(nome)
    dados.append(dado)

for item in dados:
  conversao(item)
  percentual(item, total)

total_ocupado = total / 1048576
media = total_ocupado / len(nomes)

with open ('7-exercícios-arquivos/relatório.txt', 'w', encoding='utf-8') as arquivo:
  arquivo.writelines("""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso\n
""")
  contador = int(1)
  posição = int(0)
  for item in nomes:
    arquivo.writelines(f'{contador}    {item} {dados_convertido[posição]:>7.2f} MB           {porcentagem[posição]:>6.2f}%\n')
    posição += 1
    contador += 1
  arquivo.writelines(f'\nEspaço total ocupado: {total_ocupado:.2f} MB\nEspaço médio ocupado: {media:.2f} MB')