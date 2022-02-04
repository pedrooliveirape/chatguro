from lib.horoscopo import horoscopo_dia, horoscopo_semana, verificar_ascendente
from lib.interface import menu, cabecalho
from time import sleep
from datetime import datetime
from lib.classes import Usuario

cabecalho('HORÓSCOPO', 54)
nome = str(input('Digite seu nome: '))
while True:
    data_nascimento = str(input('Digite sua data de nascimento(dd/mm/aaaa): '))
    try:
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        break
    except:
        print('\033[31mERRO!\033[m \033[33mDigite a data no formato dd/mm/aaaa (Ex: 01/01/1900).\033[m')

data_nascimento = data_nascimento.strftime('%d/%m/%Y').split('/')
usuario = Usuario(nome, int(data_nascimento[0]), int(data_nascimento[1]), int(data_nascimento[2]))
signo = usuario.signo

while True:
    resposta = menu(['Horóscopo do dia', 'Horóscopo da semana', 'Conheça seu Ascendente', 'Sair'], 54)
    if resposta == 1:
        print(f'Horóscopo do dia, \033[34m{signo[0].title()}\033[m:')
        print()
        print(horoscopo_dia(signo[1], signo[2]))
    elif resposta == 2:
        print(f'Horóscopo da semana, \033[34m{signo[0].title()}\033[m:')
        print()
        print(horoscopo_semana(signo[1], signo[2]))
    elif resposta == 3:
        ascendente = verificar_ascendente(signo[2], int(data_nascimento[0]), int(data_nascimento[1]), int(data_nascimento[2]))
        print()
        print(f'Seu ascendente é: \033[34m{ascendente}\033[m')
        print('\033[33mATENÇÃO:\033[m É importante reforçar que este método acerta em 80% dos casos. Caso você queira confirmar realmente o seu ascendente você deve fazer o seu Mapa Astral.')
    elif resposta == 4:
        print('Saindo...Até logo!')
        break
    else:
        print('Digite uma opção válida!')
    sleep(1.5)
