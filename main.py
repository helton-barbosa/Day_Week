dia = int(input('Digite um número entre 1 à 7: '))

if dia >= 1 and dia <= 7:
    if dia == 1:
        print('O dia da semana é Domingo')
    elif dia == 2:
        print('O dia da semana é Segunda-feira')
    elif dia == 3:
        print('O dia da semana é Terça-feira')
    elif dia == 4:
        print('O dia da semana é Quarta-feira')
    elif dia == 5:
        print('O dia da semana é Quinta-feira')
    elif dia == 6:
        print('O dia da semana é Sexta-feira')
    else:
        print('O dia da semana é Sábado')
else:
    print('Número inválido.')
