numero1 = float(input('Digite o 1º numero: '))
numero2 = float(input('Digite o 2º numero: '))
numero3 = float(input('Digite o 3º número: '))
numero4 = float(input('Digite o 4º número: '))
numero5 = float(input('Digite o 5º número: '))
listanumero = [numero1, numero2, numero3, numero4, numero5]
soma = 0
for numero in listanumero:
  soma = soma + numero 
else:
  media = soma / 5
  print(f'A soma dos número é: {soma}\nA média dos números é: {media}')