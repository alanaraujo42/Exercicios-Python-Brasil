class Ponto:

  def __init__(self, x, y) -> None:
    self.x = x 
    self.y = y 
  
class Retangulo:

  def __init__(self, largura, altura) -> None:
    self.largura = largura
    self.altura = altura
    self.vertice_partida = Ponto(0, 0)

def valores_ponto(ponto):
  print(f'X = {ponto.x} e Y = {ponto.y}\n')

def centro_retangulo(retangulo):
  x = retangulo.largura / 2 
  y = retangulo.altura / 2
  return x, y 


print('-- Criando um Retangulo e encontrando seu centro')
largura = float(input('Digite o tamanho da largura do retangulo: '))
altura = float(input('Digite o tamanho da altura do retangulo: '))
retangulo = Retangulo(largura, altura)
x, y = centro_retangulo(retangulo)
ponto_central = Ponto(x, y)
print(f'O centro do Retangulo é :')
valores_ponto(ponto_central)

menu = int(input('--- Menu ---\n1- Alterar valores do retangulo\n2- Finalizar Prorgama\nDigite o número correspondente a sua escolha: '))
if menu == 1:
  print('\nAlteração do Retangulo:')
  largura = float(input('Digite o tamanho da largura do retangulo: '))
  altura = float(input('Digite o tamanho da altura do retangulo: '))
  retangulo.largura = largura
  retangulo.altura = altura
  x, y = centro_retangulo(retangulo)
  ponto_central = Ponto(x, y)
  print(f'O centro do Retangulo é :')
  valores_ponto(ponto_central)
else:
  print('Fim')