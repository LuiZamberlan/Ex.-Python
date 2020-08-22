tempo = int(input('Quantos anos tem seu carro? '))

#'If' é uma estrutura de condição que avalia situações e executa uma ação de acordo com o resultado.
if tempo <=3: #Se a variável 'tempo' for maior ou igual a três, faça...
    print('Carro novo')
    #Os comandos dentro do bloco 'if' são as instruções que serão executadas de acordo com a condição especificada.

else: #Senão faça...
    print('Carro velho')

#ou->

#Condição simplificada:
print('Carro novo' if tempo <= 3 else'Carro velho')

#Outros exemplos:

nome = str(input('Nome: ')).strip().capitalize()

if nome == 'Luiz':
    print(f'Okaerinasaimase, Goshujin-sama!')

else:
    print('Seu nome é tão normal!')

#------------------------------------------------

n = float(input('primeira nota: '))
n1 = float(input('segunda nota: '))

print(f'Sua média foi de: {(n + n1) / 2:.2f}')

if ((n + n1) / 2) >= 6.0:
    print('média boa!')

else:
    print('média ruim coleguinha!')

#Simplificado:
print('Média boa!' if ((n + n1) / 2) >= 6 else 'Média Ruim!')
