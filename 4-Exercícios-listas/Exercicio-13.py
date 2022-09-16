lista_temperaturas = []
soma = float(0)
for item in range(1, 13):
  temperatura = float(input(f'Digite a temperatura do {item}º mês: '))
  soma += temperatura
  lista_temperaturas.append(temperatura)
media = soma / 12
lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outurbro', 'Novembro', 'Dezembro']
contador = int(0)
print('\n=== Temperaturas Acima da Média ===')
for item in lista_temperaturas:
  if item > media:
    print(f'\nMês: {lista_mes[contador]}\nTemperatura: {item}')
  contador += 1
