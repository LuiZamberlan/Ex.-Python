n = float(input('Primeiro segmento: '))
n1 = float(input('Segundo segmento: '))
n2 = float(input('Terceiro segmento: '))

if (n - n1) < n2 and n2 < n + n1:
    print('Os segmentos acima podem formar um triângulo!')
    #Um triângulo só existe se um de seus lados for maior que a diferença dos outro dois e menor que a soma deles.

else:
    print('Os segmentos acima não podem formar um triângulo.')
