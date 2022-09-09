print('TABAUADA V.2')
numero = int(input('Digite o número da tabuada que você deseja: '))
comeco = int(input('A tabauada deve começar em: '))
fim = int(input('A tabuada deve terminar em: '))
while fim <= comeco:
  print('\nERRO: Fim não pode ser menor que o começo\nTente Novamente!')
  fim = int(input('A tabuada deve terminar em: '))
listatabuada = list(range(comeco, fim + 1))
print('\n=== TABUADA ===')
for item in listatabuada:
  resultado = numero * item
  print(f'{numero} X {item} = {resultado}')
