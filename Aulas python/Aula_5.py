#Uma string ocupa um espaço de memória e esse espaço é separado por cada elemento presente.
frase = 'Curso em video python'
#Tem 21 elementos dentro da cadeia de caracteres na variável 'frase'

print(frase[9])
#Os elementos são organizados em índices de 0 ao último elemento, para que possamos manipular a string como uma lista

print(frase[9:14])
#É possível também selecionar uma sequência de elementos dentro da cadeia, no exemplo, começa no index 9, mas a sequencia termina no index 13, pois o index 14 é excluido da seleção

print(frase[9:21])
#O index 21 não existe, então a seleção ocorre até o ultimo elemento na cadeia.

print(frase[9:21:2])
#Esse exemplo faz com que seja selecionados elementos a cada 2

print(frase[:5])
#Aqui não indicamos onde começar a seleção, logo ele selecionará todos os elementos até o index 5

print(frase[15:])
#Da mesma forma que o exemplo anterior, a seleção começará no elemento indicado e continuará até o fim da cadeia


#Análise de strings:
print(len(frase))
#O método len() retorna a quantidade de elementos existentes na lista

print(frase.count('o'))
#A método count() indica quantos itens exigidos existem na cadeia de caracteres

print(frase.find('deo'))
#O método find() mostra a 1° ocorrência, na lista, do(s) elementos especificados

print('Curso' in frase)
#O operador 'in' mostrará se o(s) elemento(s) indicado(s) está na lista


#Transformações de listas de strings a partir de métodos
print(frase.replace('python', 'android'))
#O método replace() faz uma cópia da lista e substituindo uma parte do texto por outros elementos

print(frase.upper())
#O método upper() coloca todos os caracteres tipo alfabético em caixa alta

print(frase.lower())
#O método lower() coloca todos os caracteres tipo alfabético em minúscula

print(frase.capitalize())
#O método capitalize() coloca o 1° caracter em caixa alta e o restante da cadeia em minúscula

print(frase.title())
#O método title() faz uma quebra de palavras a partir da posição dos espaços, logo após, ele coloca o 1° caractere da palavra em maiúscula e o reto em minúscula

frase1 = '   Aprenda python   '

print(frase1)

print(frase1.strip())
#O método strip() remove todos o espaços inúteis no começo e no final da string
#O método strip() tem suas variantes: rstrip() e lstip() que tira, respectivamente e exclusivamente, somente espaços da direita e esquerda


#Divisão de string:

print(frase.split())
#O método split() separa a cadeia de caracteres a partir dos espaços no meio da string e coloca em uma lista


#Junção de string:

print(''.join(frase))
#O método join() faz a junção de uma lista de strings


#Exemplos aula:

#É possível fazer print de textos longos com """(3x Aspas duplas)
print("""Vivemos em uma época primitiva... 
nem selvagem nem sábia. Medidas paliativas são a sua maldição, 
qualquer sociedade racional ou me mataria ou faria algo de útil comigo.""")
