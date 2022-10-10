numero = input('Digite o número de telefone: ')
numero = numero.strip()
if numero:
  if '-' in numero:
    if len(numero) == 8:
      print('\nTelefone possui 7 dígitos. Vou acresentar o digito três na frente')
      numero = '3' + numero
      numero_sem_formatacao = numero.replace('-', '') 
      print(f'Telefone corrigido sem formatação: {numero_sem_formatacao}')
      print(f'Telefone corrigido com formatação: {numero}')
    else:
      print('Número Válido!')
  else:
    if len(numero) == 7:
      print('\nTelefone possui 7 dígitos. Vou acresentar o digito três na frente')
      numero = '3' + numero
      numero_com_formatacao = numero[:4] + '-' + numero[4:]
      print(f'Telefone corrigido sem formatação: {numero}')
      print(f'Telefone corrigido com formatação: {numero_com_formatacao}')
    else:
      print('Número Válido!')
else:
  print('Preencha o campo corretamente')