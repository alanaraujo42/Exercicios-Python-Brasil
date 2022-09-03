print('CAIXA ELETRÔNICO')
saque = int(input('Digite o valor que você deseja sacar: '))
while saque < 10 or saque > 600:
  print('VALOR NÃO PERMITIDO\nMínimo R$10\nMáximo R$600')
  saque = int(input('\nDigte outro valor para saque: '))
def fnota50(resto):
  nota50 = resto // 50
  print(f'{nota50} de R$50')
def fnota10(resto):
  nota10 = resto // 10
  print(f'{nota10} de R$10')
def fnota5(resto):
  nota5 = resto // 5
  print(f'{nota5} de R$5')
def fnota1(resto):
  nota1 = resto // 1
  print(f'{nota1} de R$1')
if saque >= 100:
  print('Você vai receber notas de:')
  nota100 = saque // 100
  resto = saque % 100
  print(f'{nota100} de R$100')
  if resto >= 50:
    fnota50(resto)
    resto = resto % 50
  if resto >= 10:
    fnota10(resto)
    resto = resto % 10
  if resto >= 5:
    fnota5(resto)
    resto = resto % 5
  if resto >= 1:
    fnota1(resto)
    resto = resto % 1
elif saque >= 50:
  print('Você vai receber notas de:')
  nota50 = saque // 50
  resto = saque % 50
  print(f'{nota50} de R$50')
  if resto >= 10:
    fnota10(resto)
    resto = resto % 10
  if resto >= 5:
    fnota5(resto)
    resto = resto % 5
  if resto >= 1:
    fnota1(resto)
    resto = resto % 1
elif saque >= 10:
  print('Você vai receber notas de:')
  nota10 = saque // 10
  resto = saque % 10
  print(f'{nota10} de R$10')
  if resto >= 5:
    fnota5(resto)
    resto = resto % 5
  if resto >= 1:
    fnota1(resto)
    resto = resto % 1