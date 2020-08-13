n = float(input('Qual a 1° nota? '))
n1 = float(input('Qual a 2° nota? '))

#Variável que calcula a média com as duas notas recebidas
med = (n + n1) / 2
#Utilizando o parênteses para respeitar a ordem de precedência do python

print(f'A média do aluno é {med:.1f}')
