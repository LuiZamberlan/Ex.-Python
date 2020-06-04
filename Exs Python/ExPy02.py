n=str(input('Digite o nome: '))
#Função input(): tem por objetivo de escrever a String passada como parâmetro e em seguida, ativar o modo de digitação, isto é, colocar o Console de uma determinada forma em que seja possível a digitação (entrada de dados).
#faz uma pausa no programa e espera uma entrada do usuário pelo terminal. Para ler a entrada do usuário a função input() espera que após digitada a entrada o usuário aperte a tecla enter, após isso input() lê essa entrada como uma string, portanto, se a entrada esperada for um número ela deve ser convertida usando-se as funções de conversão int() ou float().

print(f'É um prazer te conhecer, {n}')
#String literal formatada: comece uma string com f ou F, antes de abrir as aspas ou aspas triplas. Dentro dessa string, pode-se escrever uma expressão Python entre caracteres { e }, que podem se referir a variáveis, ou valores literais.

print('É um prazer te conhecer, ', n)

print('Olá {0}, é um prazer te conhecer.'.format(n))
#Método format(): serve para criar uma string que contem campos entre chaves a serem substituídos pelos argumentos de format.
