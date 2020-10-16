#Módulos: Todos os arquivos com código python são módulos, podendo ser importadas.
import math #biblioteca math, traz funções para cálculos matemáticos.
#Caso eu queira importar um função específica, podemos utilizar o from math import (função).

import random #biblioteca random pode gerar números aleatórios, embaralhar listas e sortear item de sequência.

import emoji #biblioteca para usar emojis

a = 2.5

print(math.trunc(a))
print(math.pow(2, 2))
print(math.sqrt(4))
print(math.factorial(5))

#Exemplos da aula:
num = int(input('Type a value: '))

raiz = math.sqrt(num) #Vai calcular a raiz do número recebido.
print(f'A raiz de {num} é igual a {raiz:.3f}')

print(f'A raiz de {num} é igual a {math.ceil(raiz)}')#Arredonda o valor de raiz para o número superior mais próximo.
print(f'A raiz de {num} é igual a {math.floor(raiz)}')#Arredonda o valor de raiz para o número inferior mais próximo.

#Exemplo da aula ->random:

num1 = random.random()
print(num1)

num2 = random.randint(1, 10)
print(num2)

#Exemplo da aula ->emoji:
print(emoji.emojize("Hello world! :earth_americas:", use_aliases=True))
#Utilizamos a função emojize para dar print com emoji('codigo' do emoji no site)

#Existem vários outras bibliotecas extras que estão disponíveis a download no python.org