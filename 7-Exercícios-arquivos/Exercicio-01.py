lista_ip = []
with open('7-Exercícios-arquivos/lista-ip.txt', 'r') as arquivo:
  for item in arquivo:
    ip = item.strip()
    lista_ip.append(ip)
ip_valido = []
ip_invalido = []
for ip in lista_ip:
  verificacao_ip = ip.split('.')
  validacao = True
  for parte in verificacao_ip:
    parte = int(parte)
    if parte < 0 or parte > 255:
      validacao = False
      break
  if validacao == True:
    ip_valido.append(ip)
  else:
    ip_invalido.append(ip)
with open('7-Exercícios-arquivos/verificação-ip.txt', 'w', encoding='utf-8') as arquivo:
  arquivo.write('[Endereços válidos:]\n')
  for item in ip_valido:
    arquivo.write(f'{item}\n')
  arquivo.write('\n[Endereços inválidos:]\n')
  for item in ip_invalido:
    arquivo.write(f'{item}\n')
