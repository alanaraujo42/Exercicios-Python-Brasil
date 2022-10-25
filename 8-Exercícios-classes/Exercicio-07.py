class BichinhoVirtual:

  def __init__(self, nome, idade) -> None:
    self.nome = nome
    self.fome = 5
    self.saude = 5
    self.idade = idade
  
  def alterar_nome(self, novo_nome):
    self.nome = novo_nome
  
  def alterar_fome(self, fome):
    self.fome = fome
  
  def alterar_saude(self, saude):
    self.saude = saude

  def alterar_idade(self, idade):
    self.idade = idade
  
  def humor(self):
    return self.fome + self.saude
