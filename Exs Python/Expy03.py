n = int(input('Digite um valor: '))
#Função int(): converte um dado string para um número inteiro. O string deve ser algo como "123" ou "-5", pois senão ocorrerá um erro.

n1 = int(input('Digite outro valor: '))

s = n + n1

print('A soma entre {0} e {1} é igual a {2}!'.format(n,n1,(n+n1)))

print('A soma entre {0} e {1} é igual a {2}!'.format(n,n1,s))

print(f'A soma entre {n} e {n1} é igual a {n+n1}!')

print(f'A soma entre {n} e {n1} é igual a {s}!')
