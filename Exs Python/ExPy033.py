n = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))
n2 = int(input('Digite mais outro valor: '))

#Qual o menor valor:
mn = n

if n1 < n and n1 < n2:
    mn = n1
if n2 < n and n2 < n1:
    mn= n2

#Qual o maior valor:
mr = n

if n1 > n and n1 > n2:
    mr = n1
if n2 > n and n2 > n1:
    mr = n2

print(f'O maior número é {mr}')
print(f'O menor número é {mn}')
