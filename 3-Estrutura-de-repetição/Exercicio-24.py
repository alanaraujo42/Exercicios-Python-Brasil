print('MÉDIA DAS NOTAS')
resposta = 'sim'
listadenotas = []
while resposta == 'sim':
  nota = float(input("Digite a nota: "))
  listadenotas.append(nota)
  resposta = str.lower(input('Deseja adicionnar outra nota (Sim ou Não): '))
soma = float(0)
for item in listadenotas:
  soma = soma + item
media = soma / (len(listadenotas))
print(f'\nA média das notas é: {media:.2f}')