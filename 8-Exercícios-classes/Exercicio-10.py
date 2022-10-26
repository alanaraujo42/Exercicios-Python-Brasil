class BombaCombusticel:

  def __init__(self, tipo_combustivel, valor_litro, quantidade) -> None:
    self.tipo_combustivel = tipo_combustivel
    self.valor_litro = valor_litro
    self.qtde_combustivel = quantidade
  
  def abastecer_por_valor(self, valor):
    total_litro = valor / self.valor_litro
    if total_litro < self.qtde_combustivel:
      self.qtde_combustivel -= total_litro
      print(f'Foi abastecido {total_litro:.2f} litros')
    else:
      print('Quantidade de combustível na bomba insuficiente')
  
  def abastecer_por_litro(self, valor):
    if valor < self.qtde_combustivel:
      total_valor = valor * self.valor_litro
      self.qtde_combustivel -= valor
      print(f'O valor a ser pago é de {total_valor:.2f}')
    else:
      print('Quantidade de combustível na bomba insuficiente')
  
  def alterar_valor(self, novo_valor):
    self.valor_litro = novo_valor
  
  def alterar_combustivel(self, novo_combustivel):
    self.tipo_combustivel = novo_combustivel
  
  def alterar_qtde_combustivel(self, nova_qtde):
    self.qtde_combustivel = nova_qtde
  