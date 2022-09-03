print('REGULAMENTO DE PESCA')
peso = float(input('Digite o peso do peixe: '))
excesso = float(peso - 50)
multa = float(excesso * 4)
if excesso < 1:
  print(f'O peso do peixe é de {peso}Kg, não excedeu o limite permitido de 50Kg \nNão há necessidade de pagar multa')
else:
  print(f'O peso do peixe é de {peso} e ele excedeu o limite permitido de 50Kg')
  print(f'O excesso é de {excesso:.2f}Kg e o valor da multa é de: R${multa:.2f}')