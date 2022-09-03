print('NOME DE USUÁRIO E SENHA')
usuario = input('Digite um nome de usuário: ')
senha = input('Digite uma senha: ')
while usuario == senha:
  print('\nERRO: Usuário e Senha não podem ser iguais!\nTente novamente\n')
  usuario = input('Digite um nome de usuário: ')
  senha = input('Digite uma senha: ')