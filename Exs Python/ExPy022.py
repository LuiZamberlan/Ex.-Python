n = str(input('Qual seu nome? '))

print(f'Seu nome em maiúsculas: {n.upper()}')

print(f'Seu nome em minúsculas: {n.lower()}')

ql = len(n) - n.count(' ')
#ql irá contar o número de elementos da variável 'n' e irá subtrair os espaços contador pelo count()
print(f'Seu nome tem {ql} letras')
#Total de letras do 'n' sem os espaços

ql1 = n.replace(' ', '')
#ql1 irá tirar os espaços na variável 'n' (substituir os espaços por nada)
print(f'Seu nome tem {len(ql1)} letras')
#Total de letras do 'n' sem espaços

#o split irá colocar o nome inteiro e separado em uma lista e o len irá exibir o total de caracteres do index 0 dessa lista
print(f'Seu primeiro nome tem {len(n.split()[0])} letras')

a = n.find(' ')
#'a' irá exibir o index de início dos elementos ' '(espaço)
print(f'Seu primeiro nome tem {a} letras')
#No print() o 'a' será o resultado do len do 1° nome recebido em 'n'