print('CRESCIMENTO DE POPULAÇÃO DO PAÍS!')
população_a = int(80000)
população_b = int(200000)
crescimento_a = 3 / 100
crescimento_b = 1.5 / 100
ano = int(0)
while população_a < população_b:
  população_a = int(população_a + (população_a * crescimento_a))
  população_b = int(população_b + (população_b * crescimento_b))
  ano = ano + 1
  print(população_a, população_b)
print(f'A população do País A vai precisar de {ano} anos')