def ln(t = 1):
    #função que quando executada mostrará uma linha conforme o valor recebido em t. Criada como teste de uso de funções, para diminuir o número de comandos print na tela  e para poupar trabalho de reescrever a função print novamente(preguiça que chama :p )

    if t == 0:
        print('=' * 30)
    elif t == 1:
        print('-' * 30)
    elif t == 2:
        print('-=' * 30)


#Supondo que queremos escrever uma mensagem(um tipo de dado), para isso, precisaremos de delimitadores especiais para mensagens, o delimitador padrão do python nessa situação é aspas["(duplas);'(simples)] e para executar a ação de escrever essa mensagem, utilizamos a função print().

ln(2)

#Exemplo:
print('Olá, mundo!')

#Parte prática

print('Olá, ' + 'Mundo!')
#Utilizando o mais(+) podemos juntar uma mensagem(dado tipo string) a outra e caso o tipo de dado for numérico como números inteiros, podemos utilizar o mais para operações matemáticas(quando não colocados as aspas).

#Exemplo
print(1 + 1)#Resultado -> 2 (dado tipo int)

print('1' + '1')#Resultado -> '11' (dado tipo str)

ln(2)

#Podemos incluir variáveis para que seja possível o uso de informações de forma mais complexa, como por exemplo, podemos deixar registrado qualquer tipo de dado nelas e logo, manipular os dados para que sejam exibidos da maneira que queremos.

#Exemplo
nome = 'Luiz'
#A variável (nome) recebe(=) 'Luiz'(dado tipo str)
type(nome)#<class 'str'>
idade = 24
#A variável (idade) recebe(=) 26(dado tipo int)
type(idade)#<class 'int'>
peso = 62.5
#A variável (peso) recebe(=) 62.5(dado tipo float)
type(peso)#<class 'float'>

print(nome, idade, peso)

ln()

#Agora com mais interatividade, podemos fazer com que o programa registre a entrada de um dado, permitir que digitem os dados utilizando a função input()

nome = input('Qual o seu nome? ')
#Recebe do teclado um dado tipo 'str'
idade = input('Qual sua idade? ')
#Também recebe um dado tipo 'str'(por mais que seja digitado um número), pois, quando não especificado o tipo de dado[Exemplo: int(input())] que o input irá receber, ele automaticamente receberá um dado tipo str(não importa se é numérico ou não)
peso = input('Qual o seu peso? ')

print(nome, idade, peso)

ln(2)

#Desafios da aula ->
print('Desafio 01')
Nome = str(input('Digite seu nome? '))
print('Seja muito bem vindo ao mundo da programação', Nome, '!')
print('Seja muito bem vindo {0}, ao mundo da programação!'.format(Nome))
print(f'Seja muito bem vindo {Nome}, ao mundo da programação!')

ln(0)

print('Desafio 02')
dia = int(input('Qual dia você nasceu? '))
mes = int(input('De que mês? '))
ano = int(input('E de que ano? '))
print('Data de nascimento: {0}/{1}/{2}'.format(dia, mes, ano))
print(f'Data de nascimento: {dia}/{mes}/{ano}')

ln(0)

print('Desafio 03')
n0 = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))
print('A soma de {0} e {1} é {2}'.format(n0, n1, (n0 + n1)))
print(f'{n0} + {n1} = {n0 + n1}')

ln()

#Ou -->

n2 = int(input('Type a value: '))
n3 = int(input('Type another value: '))

s = n2 + n3

print('{0} + {1} = {2}'.format(n2, n3, s))
print(f'{n2} + {n3} = {s}')
