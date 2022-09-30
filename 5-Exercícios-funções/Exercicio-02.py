def função(item):
  for vezes in range(1, item + 1):
    for i in range(1, vezes + 1):
      print(f'{i} ', end='')
    print('')
n = int(input('Digite um número: '))
função(n)