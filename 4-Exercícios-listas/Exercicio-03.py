notas = []
soma = float(0)
for item in range(1, 5):
  nota = float(input(f'Digite a {item}º nota: '))
  notas.append(nota)
  soma += nota
media = soma / 4
print(f'\nAs notas foram: {notas}\nA média é: {media}')