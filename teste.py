from datetime import datetime, timedelta

signo = 4
ano = 1988
mes = 7
dia = 27

while True:
    input_hora_nascimento = str(input('Digite a hora do seu nascimento (hh:mm): '))
    input_hora_nascimento = f'{dia}/{mes}/{ano} ' + input_hora_nascimento
    print(input_hora_nascimento)
    try:
        hora_nascimento = datetime.strptime(input_hora_nascimento, '%d/%m/%Y %H:%M')
        break
    except:
        print('\033[31mERRO!\033[m \033[33mDigite o horário no formato 24h hh:mm (exemplo: 23:59)\033[m')

hora_teste = datetime(ano, mes, dia, 00, 30)
print(hora_teste)

soma_hora = timedelta(hours=+2)

cont = 0
while True:
    if hora_nascimento <= hora_teste and cont == 0:
        horario = '22:31 as 0:30'
        break
    elif hora_nascimento <= hora_teste:
        horario = f'{cont - 2}:31 as {cont}:30'
        break
    else:
        cont += 2
        hora_teste += soma_hora
print(horario)

matriz_ascendente = [
    {'6:31 as 8:30': 'Áries', '8:31 as 10:30': 'Touro', '10:31 as 12:30': 'Gêmeos', '12:31 as 14:30': 'Câncer',
     '14:31 as 16:30': 'Leão', '16:31 as 18:30': 'Virgem', '18:31 as 20:30': 'Libra', '20:31 as 22:30': 'Escorpião',
     '22:31 as 0:30': 'Sagitário', '0:31 as 2:30': 'Capricórnio', '2:31 as 4:30': 'Aquário',
     '4:31 as 6:30': 'Peixes'},
    {'6:31 as 8:30': 'Touro', '8:31 as 10:30': 'Gêmeos', '10:31 as 12:30': 'Câncer', '12:31 as 14:30': 'Leão',
     '14:31 as 16:30': 'Virgem', '16:31 as 18:30': 'Libra', '18:31 as 20:30': 'Escorpião',
     '20:31 as 22:30': 'Sagitário', '22:31 as 00:30': 'Capricórnio', '0:31 as 2:30': 'Aquário',
     '2:31 as 4:30': 'Peixes', '4:31 as 6:30': 'Áries'},
    {'6:31 as 8:30': 'Gêmeos', '8:31 as 10:30': 'Câncer', '10:31 as 12:30': 'Leão', '12:31 as 14:30': 'Virgem',
     '14:31 as 16:30': 'Libra', '16:31 as 18:30': 'Escorpião', '18:31 as 20:30': 'Sagitário',
     '20:31 as 22:30': 'Capricórnio', '22:31 as 0:30': 'Aquário', '0:31 as 2:30': 'Peixes',
     '2:31 as 4:30': 'Áries', '4:31 as 6:30': 'Touro'},
    {'6:31 as 8:30': 'Câncer', '8:31 as 10:30': 'Leão', '10:31 as 12:30': 'Virgem', '12:31 as 14:30': 'Libra',
     '14:31 as 16:30': 'Escorpião', '16:31 as 18:30': 'Sagitário', '18:31 as 20:30': 'Capricórnio',
     '20:31 as 22:30': 'Aquário', '22:31 as 0:30': 'Peixes', '0:31 as 2:30': 'Áries', '2:31 as 4:30': 'Touro',
     '4:31 as 6:30': 'Gêmeos'},
    {'6:31 as 8:30': 'Leão', '8:31 as 10:30': 'Virgem', '10:31 as 12:30': 'Libra', '12:31 as 14:30': 'Escorpião',
     '14:31 as 16:30': 'Sagitário', '16:31 as 18:30': 'Capricórnio', '18:31 as 20:30': 'Aquário',
     '20:31 as 22:30': 'Peixes', '22:31 as 0:30': 'Áries', '0:31 as 2:30': 'Touro', '2:31 as 4:30': 'Gêmeos',
     '4:31 as 6:30': 'Câncer'},
    {'6:31 as 8:30': 'Virgem', '8:31 as 10:30': 'Libra', '10:31 as 12:30': 'Escorpião',
     '12:31 as 14:30': 'Sagitário', '14:31 as 16:30': 'Capricórnio', '16:31 as 18:30': 'Aquário',
     '18:31 as 20:30': 'Peixes', '20:31 as 22:30': 'Áries', '22:31 as 0:30': 'Touro', '0:31 as 2:30': 'Gêmeos',
     '2:31 as 4:30': 'Câncer', '4:31 as 6:30': 'Leão'},
    {'6:31 as 8:30': 'Libra', '8:31 as 10:30': 'Escorpião', '10:31 as 12:30': 'Sagitário',
     '12:31 as 14:30': 'Capricórnio', '14:31 as 16:30': 'Aquário', '16:31 as 18:30': 'Peixes',
     '18:31 as 20:30': 'Áries', '20:31 as 22:30': 'Touro', '22:31 as 0:30': 'Gêmeos', '0:31 as 2:30': 'Câncer',
     '2:31 as 4:30': 'Leão', '4:31 as 6:30': 'Virgem'},
    {'6:31 as 8:30': 'Escorpião', '8:31 as 10:30': 'Sagitário', '10:31 as 12:30': 'Capricórnio',
     '12:31 as 14:30': 'Aquário', '14:31 as 16:30': 'Peixes', '16:31 as 18:30': 'Áries', '18:31 as 20:30': 'Touro',
     '20:31 as 22:30': 'Gêmeos', '22:31 as 0:30': 'Câncer', '0:31 as 2:30': 'Leão', '2:31 as 4:30': 'Virgem',
     '4:31 as 6:30': 'Libra'},
    {'6:31 as 8:30': 'Sagitário', '8:31 as 10:30': 'Capricórnio', '10:31 as 12:30': 'Aquário',
     '12:31 as 14:30': 'Peixes', '14:31 as 16:30': 'Áries', '16:31 as 18:30': 'Touro', '18:31 as 20:30': 'Gêmeos',
     '20:31 as 22:30': 'Câncer', '22:31 as 0:30': 'Leão', '0:31 as 2:30': 'Virgem', '2:31 as 4:30': 'Libra',
     '4:31 as 6:30': 'Escorpião'},
    {'6:31 as 8:30': 'Capricórnio', '8:31 as 10:30': 'Aquário', '10:31 as 12:30': 'Peixes',
     '12:31 as 14:30': 'Áries', '14:31 as 16:30': 'Touro', '16:31 as 18:30': 'Gêmeos', '18:31 as 20:30': 'Câncer',
     '20:31 as 22:30': 'Leão', '22:31 as 0:30': 'Virgem', '0:31 as 2:30': 'Libra', '2:31 as 4:30': 'Escorpião',
     '4:31 as 6:30': 'Sagitário'},
    {'6:31 as 8:30': 'Aquário', '8:31 as 10:30': 'Peixes', '10:31 as 12:30': 'Áries', '12:31 as 14:30': 'Touro',
     '14:31 as 16:30': 'Gêmeos', '16:31 as 18:30': 'Câncer', '18:31 as 20:30': 'Leão', '20:31 as 22:30': 'Virgem',
     '22:31 as 0:30': 'Libra', '0:31 as 2:30': 'Escorpião', '2:31 as 4:30': 'Sagitário', '4:31 as 6:30': 'Capricórnio'},
    {'6:31 as 8:30': 'Peixes', '8:31 as 10:30': 'Áries', '10:31 as 12:30': 'Touro', '12:31 as 14:30': 'Gêmeos',
     '14:31 as 16:30': 'Câncer', '16:31 as 18:30': 'Leão', '18:31 as 20:30': 'Virgem', '20:31 as 22:30': 'Libra',
     '22:31 as 0:30': 'Escorpião', '0:31 as 2:30': 'Sagitário', '2:31 as 4:30': 'Capricórnio',
     '4:31 as 6:30': 'Aquário'}
]

ascendente = str(matriz_ascendente[signo][horario])
print(ascendente)
