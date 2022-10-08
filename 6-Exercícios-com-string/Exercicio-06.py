from calendar import day_abbr


mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data_nascimento = input('Digite a sua data de nascimento (dd/mm/aaaa): ')
data_nascimento = data_nascimento.split('/')
data_nascimento[1] = mes[int(data_nascimento[1]) - 1]
data_nascimento = ' de '.join(data_nascimento)
print(f'Você nasceu em {data_nascimento}.')