from random import choice
def verificacao():
  linha_1 = ma_teste[0] + ma_teste[1] + ma_teste[2]
  linha_2 = ma_teste[3] + ma_teste[4] + ma_teste[5]
  linha_3 = ma_teste[6] + ma_teste[7] + ma_teste[8]
  diagonal_1 = ma_teste[0] + ma_teste[4] + ma_teste[8]
  diagonal_2 = ma_teste[2] + ma_teste[4] + ma_teste[6]
  coluna_1 = ma_teste[0] + ma_teste[3] + ma_teste[6]
  coluna_2 = ma_teste[1] + ma_teste[4] + ma_teste[7]
  coluna_3 = ma_teste[2] + ma_teste[5] + ma_teste[8]
  if linha_1 == linha_2 == linha_3 == diagonal_1 == diagonal_2 == coluna_1 == coluna_2 == coluna_3 and ma_teste not in matriz_aprovada:
    matriz_aprovada.append(ma_teste)
    print(f'''
{ma_teste[0]} {ma_teste[1]} {ma_teste[2]}
{ma_teste[3]} {ma_teste[4]} {ma_teste[5]}
{ma_teste[6]} {ma_teste[7]} {ma_teste[8]}
''')

matriz_aprovada = []
for _ in range(1088640):
  seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  ma_teste = []
  for _ in range(9):
    x = choice(seq)
    ma_teste.append(x)
    seq.remove(x)
  verificacao()