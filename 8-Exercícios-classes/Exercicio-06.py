class Tv:

  def __init__(self) -> None:
    self.canal = 10
    self.volume = 10
  
  def mudar_canal(self, canal):
    if canal >=1 and canal <=100:
      self.canal = canal
    else:
      print('Canal Inválido')
  
  def aumentar_volume(self):
    if self.volume >= 100:
      print('Limite máximo do volume')
    else:
      self.volume += 1
  
  def diminuir_volume(self):
    if self.volume <= 0:
      print('Limite mínimo do volume')
    else:
      self.volume -= 1
