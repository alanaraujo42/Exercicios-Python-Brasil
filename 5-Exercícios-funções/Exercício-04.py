def analise(item):
  if item > 0:
    return 'P'
  else:
    return 'N'
n = float(input('Digite um número: '))
resultado = analise(n)
print(resultado)