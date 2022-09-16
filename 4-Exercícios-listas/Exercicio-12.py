lista_altura = []
soma = float(0)
for item in range(1, 31):
  print(f'\n=== {item}º Aluno ===')
  idade = int(input('Digite a idade: '))
  altura = float(input('Digite a altura: '))
  if idade > 13:
    lista_altura.append(altura)
  soma += altura
media = soma / 30
resultado = int(0)
for item in lista_altura:
  if item < media:
    resultado += 1
print(f'\n{resultado} aluno(s) com altura inferior a média')