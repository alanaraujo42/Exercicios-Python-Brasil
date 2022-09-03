print('FOLHA DE PAGAMENTO')
valorhora = float(input('Digite o valor da sua hora de trabalho: R$'))
horastrabalho = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salariobruto = float(valorhora * horastrabalho)
if salariobruto <= 900:
  percentual = 0
  ir = float(0)
elif salariobruto <= 1500:
  percentual = 5
  ir = float(salariobruto * 5 /100)
elif salariobruto <= 2500:
  percentual = 10
  ir = float(salariobruto * 10 /100)
elif salariobruto > 2500:
  percentual = 20
  ir = float(salariobruto * 20 /100)
sindicato = float(salariobruto * 3 /100)
fgts = float(salariobruto * 11 /100)
descontos = ir + sindicato
salarioliquido = salariobruto - descontos
print(f'\nSalário Bruto: R${salariobruto}')
print(f'\nDesconto do IR ({percentual}%): R${ir}\nDesconto do Sindicato (3%): R${sindicato}')
print(f'Valor do FGTS (11%): R${fgts}')
print(f'Total de descontos: R${descontos}')
print(f'\nSalário Líquido: R${salarioliquido}')