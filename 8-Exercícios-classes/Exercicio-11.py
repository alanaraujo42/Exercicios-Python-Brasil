class Carro:

  def __init__(self, consumo) -> None:
    self.consumo_km_l = consumo
    self.combustivel = 0
  
  def andar(self, km):
    consumo_combustivel = km / self.consumo_km_l
    if consumo_combustivel > self.combustivel:
      print('Combustível Insuficiente!')
    else:
      self.combustivel -= consumo_combustivel
  
  def obter_gasolina(self):
    print(f'O carro tem {self.combustivel:.2f} litros de gasolina')
  
  def adicionar_gasolina(self, litro):
    self.combustivel += litro