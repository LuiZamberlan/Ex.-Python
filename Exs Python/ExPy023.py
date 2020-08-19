n = int(input('Digite um número de 0 a 9999: '))

u = n % 10
#O resto da divisão desse número por 10 é igual a unidade do número recebido

d = n // 10 % 10
#O número recebido na divisão inteira por 10 exclui a unidade, logo depois, no resto da divisão por 10 obtemos a dezena

c = n // 100 % 10

m = n // 1000 % 10

print(f'milhar: {m} centena: {c} dezena: {d} unidade: {u}')
