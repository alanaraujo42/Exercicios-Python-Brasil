class Macaco:

  def __init__(self, nome) -> None:
    self.nome = nome
    self.bucho = []
  
  def comer(self, comida):
    self.bucho.append(comida)

  def ver_bucho(self):
    print('Comida no bucho: ')
    for i in self.bucho:
      print(i)
  
  def digerir(self):
    print('Digerindo...')
    self.bucho = []
