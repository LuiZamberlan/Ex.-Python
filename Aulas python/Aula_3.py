#Operadores aritméticos do python: Iguais aos de matemáticos.
# + (adição)
a=5 + 2
# - (subtração)
b=5 - 2
# * (multiplicação)
c=5 * 2
# / (divisão)
d=5 / 2

print(f'5 + 2 = {a}')
print(type(a))

print(f'5 - 2 = {b}')
print(type(b))

print(f'5 * 2 = {c}')
print(type(c))

print(f'5 / 2 = {d}')
print(type(d))

# ** (exponenciação)
e = 5 ** 2
# // (parte inteira da divisão)
f = 5 // 2
# % (módulo, resto de uma divisão)
g = 5 % 2

print(f'5 ** 2 = {e}')
print(type(e))

print(f'5 // 2 = {f}')
print(type(f))

print(f'5 % 2 = {g}')
print(type(g))

#Ordem de precedência: 1° () tudo que está em parênteses; 2° **; 3° *, /, //, %; 4° +, -.

#Exemplos:

print(5 + 3 * 2)#primeiro a multiplicação, depois a adição

print(3 * 5 + 4 ** 2)#primeiro a exponenciação, depois multiplicação e logo após, a adição

print(3 * (5 + 4) ** 2)#primeiro o que está entre parênteses, depois a exponenciação, em seguida, a multiplicação

#Também é possível usar alguns operadores com strings:

#utilizando o operador de adição (contatenação)
print('Olá' + 'Oi!')

#operador de multiplicação
print('Olá' * 5)

#Preenchimento em formatação:
#Variável que recebe o nome:
nome = str(input('Nome: '))

#preenchimento do nome em 20 espaços
print(f'Prazer em te conhecer {nome :20}!')

#preenchimento do nome em 20 espaços, posicionado a direita
print(f'Prazer em te conhecer {nome :>20}!')

#preenchimento do nome em 20 espaços, posicionado a esquerda
print(f'Prazer em te conhecer {nome :<20}!')

#preenchimento do nome em 20 espaços, posicionado ao centro
print(f'Prazer em te conhecer {nome :^20}!')

#preenchimento do nome em 20 "=", posicionado ao centro
print(f'Prazer em te conhecer {nome :=^20}!')

#Também é possível limitar o número de casas decimais em de valores tipo float:
na1 = 10/3

print(f'o número é {na1:.3f}')#3 é o número de casas decimais que irá ser exibida