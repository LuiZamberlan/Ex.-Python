v = int(input('Qual a velocidade do carro? '))

if v > 80:
    print(f'Você está sendo multado em R${float((v - 80) * 7):.2f}')
    #Subtraindo o valor 'v' por 80, teremos quanto km/h excedeu e multiplicamos por 7

else:
    print('Está tudo certo! Tenha um bom dia!')
