#Tipos primitivos de dados básicos de python são: int(números inteiros), float(números reais ou de ponto flutuante(forma decimal)), bool(valores lógicos) e str(valores caracteres).

n = input('Digite um valor: ')
#Variável n vai receber um valor pelo teclado, mas como o tipo de dado não está especificado, o valor recebido será do tipo string.

print(type(n))
#Esse print confirmará que tipo de dado é.

n0 = int(input('Digite um valor: '))
#Variável n0 vai receber um valor pelo teclado e como o tipo especificado é um dado tipo inteiro, então só receberá dados desse tipo, caso colocado outro tipo de valor ele resultará em erro.

print(type(n0))
#Confirmação do tipo de dado.

n1 = float(input('Digite um valor: '))
#A variável n1 vai receber um valor pelo teclado do tipo float, mas ainda é possível escrever um valor do tipo inteiro, pois logo que recebido o valor ele converterá para um dado tipo float, mas isso só funciona para o dado tipo int.

print(type(n1))

#Quando temos um valor tipo string podemos testar se ele é numérico ou alfabético(ou ambos), se ele é alfabético e está com caracteres em maiúsculas ou em minúsculas e por ai vai. Tudo isso com o .is, que em um print() terá como resposta True ou False.
valor = input('Digite algo: ')
valor1 = input('Digite outra coisa: ')
valor2 = input('Digite algo a mais: ')

#Exemplos
print(valor.isalpha())#se ele é alfabético
print(valor1.isnumeric())#se ele é numérico
print(valor2.isalnum())#se ele é alfanumérico
