print('FATORIAL DE UM NÚMERO INTEIRO V.2')
resposta = str('sim')
while resposta == 'sim':
  numero = int(input('Digite um número: '))
  while numero < 0 or numero >= 16:
    print('ERRO: Só pode números inteiros positivos e menores que 16\nTente Novamente\n')
    numero = int(input('Digite um número: '))
  resultado = numero
  while numero > 1:
    resultado = resultado * (numero - 1)
    numero = numero - 1
  print(f'O resultado da fatorial é {resultado}')
  resposta = str.lower(input('\nDeseja calcular a fatorial de outro número? (SIM ou NÃO)\n:'))