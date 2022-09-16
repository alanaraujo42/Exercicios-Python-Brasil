# VERSÃO PARA LER UMA LETRA
lista = []
consoantes = int(0)
for item in range(1, 11):
  caractere = str.lower(input('Digite uma letra: '))
  if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
    pass
  else:
    consoantes += 1
    lista.append(caractere)
print(f'\nForam lidas {consoantes} consoantes\nElas são: {lista}')


# VERSÃO PARA LER UMA PALAVRA
# consoante = int(0)
# lista_consoante = []
# for contador in range(1, 11):
#   caractere = str.lower(input('Digite uma palavra: '))
#   lista = list(range(0, len(caractere)))
#   for item in lista:
#     x = caractere[item]
#     if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#       pass
#     else: 
#       consoante += 1
#       lista_consoante.append(x)
# print(f'\nForam lidas {consoante} consoantes\nElas são: {lista_consoante}')