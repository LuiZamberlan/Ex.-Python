qd = int(input('Quantos dias você ficou com o carro? '))
qk = float(input('Quantos kilometros o carro andou? '))

#Total a pagar soma o preço do aluguel por dia com o preço do aluguel por km rodado
tp = (qd * 60) + (qk * 0.15)

print(f'No total, você precisa pagar R${tp:.2f}')