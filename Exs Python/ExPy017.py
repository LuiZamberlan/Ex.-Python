from math import hypot
#Função que calcula a hipotenusa utilizando valores recebidos como cateto oposto e adjacente

co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))

#A hipotenusa pode ser calculada pela soma dos catetos elevado a potência 2
hip = ((co ** 2) + (ca ** 2)) ** (1/2)

print(f'A hipotenusa vai medir: {hip:.2f}')

#Exemplo da aula:

print(f'A hipotenusa vai medir: {hypot(co, ca):.2f}')
