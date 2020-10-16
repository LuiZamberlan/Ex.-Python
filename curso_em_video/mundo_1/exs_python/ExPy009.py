nt = int(input('Digite um número inteiro para exibir a tabuada: '))

#Variável que irá somar a cada vez que o loop for executado, para multiplicar na tabela
nq = 1

print('-' * 20)

#Loop (for) que irá repetir o ciclo dez vezes.
for i in range(10):
    print(f'{nt} x {nq} = {nt * nq}')
    #nq = nq + 1
    nq+=1

print('-' * 20)

#Versão da resolução do exercício
print('-' * 20)

print(f'{nt} x  1 = {nt * 1}')
print(f'{nt} x  2 = {nt * 2}')
print(f'{nt} x  3 = {nt * 3}')
print(f'{nt} x  4 = {nt * 4}')
print(f'{nt} x  5 = {nt * 5}')
print(f'{nt} x  6 = {nt * 6}')
print(f'{nt} x  7 = {nt * 7}')
print(f'{nt} x  8 = {nt * 8}')
print(f'{nt} x  9 = {nt * 9}')
print(f'{nt} x 10 = {nt * 10}')

print('-' * 20)
