def desenho(linha, coluna):
  if linha > 20: 
    linha = 20
  elif linha < 1: 
    linha = 1
  if coluna > 20: 
    coluna = 20
  elif coluna < 1:
    coluna = 1
  print(' -' * coluna)
  for _ in range(0, linha):
    print('|', '  ' * (coluna - 1), '|' )
  print(' -' * coluna)
linha = int(input('Digite o número de linhas: '))
coluna = int(input('Digite o número de colunas: '))
desenho(linha, coluna)