class Quadrado:

  def __init__(self) -> None:
    self.lado = 4

  def mudar_valor_lado(self, valor):
    self.lado = valor
  
  def consultar_valor_lado(self):
    print(f'O tamanho do lado é {self.lado}')

  def calcular_area(self):
    area = self.lado ** 2
    print(f'A área do quadrado é de {area}')
