class Bola:

  def __init__(self):
    self.cor = None
    self.circunferencia = None
    self.material = None
    print('Inicio')
  
  def trocar_cor(self, cor):
    self.cor = cor
  
  def mostrar_cor(self):
    print(f'A cor da bola é {self.cor}')