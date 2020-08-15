from math import trunc
#Função truncate

n = float(input('Type any value: '))

print(f'O número {n} tem a parte inteira {trunc(n)}')
#Função Trunc() coloca é uma forma de conseguir a parte inteira de um número, ele age como um ceil() para números negativos e como um floor() para números positivos.
