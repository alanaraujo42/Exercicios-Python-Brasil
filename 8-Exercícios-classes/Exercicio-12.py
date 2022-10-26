class ContaInvestimento:

  def __init__(self, saldo, taxa_juros) -> None:
    self.saldo = saldo
    self.taxa_juros = taxa_juros
  
  def adicione_juros(self):
    self.saldo += self.saldo / self.taxa_juros
  

poupanca = ContaInvestimento(1000, 10)
poupanca.adicione_juros()
poupanca.adicione_juros()
poupanca.adicione_juros()
poupanca.adicione_juros()
poupanca.adicione_juros()
print(f'O saldo é de R${poupanca.saldo:.2f}')