def soma_imposto(taxa_imposto, custo):
  resultado = custo + (taxa_imposto * custo / 100)
  return resultado
taxa = float(input('Digite a texa do imposto (%): '))
custo = float(input('Digite o custo do item: R$'))
resultado = soma_imposto(taxa, custo)
print(f'O custo com a taxa fica de: R${resultado:.2f}')