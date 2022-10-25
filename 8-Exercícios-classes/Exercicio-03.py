class Retangulo:

  def __init__(self, base, altura) -> None:
    self.base = base
    self.altura = altura

  def mudar_base(self, valor):
    self.base = valor

  def mudar_altura(self, valor):
    self.altura = valor
  
  def consultar_base(self):
    print(f'A base do Retangulo é de {self.base}')
  
  def consultar_altura(self):
    print(f'A altura do Retangulo é de {self.altura}')
  
  def calcular_area(self):
    return self.base * self.altura
  
  def calcular_perimetro(self):
    return 2 * (self.base + self.altura)

#Programa
base = float(input('Digite a tamanho da base um local: '))
altura = float(input('Digite o tamanho da altura de um local: '))
local = Retangulo(base, altura)
print(f'Para o local é necessário {local.calcular_area()}m² de piso e {local.calcular_perimetro()}m de rodapés')
