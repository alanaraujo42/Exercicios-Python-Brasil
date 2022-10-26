class Funcionario:

  def __init__(self, nome, salario) -> None:
    self.nome = nome
    self.salario = salario
  
  def mostrar_nome(self):
    print(f'O nome do(a) funcionário(a) é {self.nome}')
  
  def mostrar_salario(self):
    print(f'O salário do(a) funcionário(a) é {self.salario}')

pessoa = Funcionario('Maria', 2000)
pessoa.mostrar_nome()
pessoa.mostrar_salario()