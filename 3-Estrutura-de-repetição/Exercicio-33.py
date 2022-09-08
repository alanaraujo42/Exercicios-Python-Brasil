print('LEITURA DE TEMPERATURAS')
temperatura = float(input('Digite a temperatura: '))
resposta = str.lower(input('Deseja adicionar outra temperatura (Sim ou Não): '))
menor = temperatura
maior = temperatura
soma = temperatura
contador = int(1)
while resposta == 'sim':
  temperatura = float(input('\nDigite a temperatura: '))
  soma += temperatura
  contador += 1
  if temperatura > maior:
    maior = temperatura
  elif temperatura < menor:
    menor = temperatura
  resposta = str.lower(input('Deseja adicionar outra temperatura (Sim ou Não): '))
media = soma / contador
print(f'\nA menor temperatura é {menor}\nA maior temperatura é {maior}\nA média das temperaturas é {media:.2f}')