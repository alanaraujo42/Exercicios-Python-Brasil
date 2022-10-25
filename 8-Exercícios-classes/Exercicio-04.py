class Pessoa:

  def __init__(self, nome, idade, peso, altura) -> None:
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
  
  def envelhercer(self, valor = 1):
    if self.idade < 21:
      self.idade += valor
      self.altura += 0.5
    else:
      self.idade += valor
  
  def engordar(self, valor = 1):
    self.peso += valor
  
  def emagrecer(self, valor = 1):
    self.peso -= valor
  
  def crescer(self, valor = 0.1):
    self.altura += valor
