def função(item):
  for vezes in range(0, item + 1):
    print(f'{vezes} ' * vezes)

n = int(input('Digite um número: '))
função(n)