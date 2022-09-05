print('SÉRIE DE FIBONACCI ATÉ 500')
ultimo = int(1)
penultimo = int(0)
while ultimo <= 500:
  print(ultimo)
  meio = ultimo
  ultimo = ultimo + penultimo
  penultimo = meio
  if ultimo > 500:
    print(ultimo)