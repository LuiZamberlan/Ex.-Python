from random import shuffle

a = str(input('Nome do aluno 0: '))
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))

list = [a, a1, a2, a3]

shuffle(list)
#Função shuffle embaralha a 'list'

print(list)
