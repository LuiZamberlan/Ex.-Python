from datetime import date
a = int(input('Que ano quer analisar? digite 0 parao  ano atual: '))

if a == 0:
    a = date.today().year
    #'a' recebe o ano atual da máquina

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    #Se o 'a' for divisível por 4 e não for divisível por 100, é um ano bissexto.
    print(f'{a} é um ano bissexto.')

else:
    print(f'O ano {a} não é bissexto.')
