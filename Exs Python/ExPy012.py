p = float(input('Informe o valor do produto: R$'))

#O desconto é calculado pelo valor do produto - 5% do valor total dele.
d = p - ((p * 5) / 100)

print(f'O produto com desconto da promoção custa: R${d:.2f}')
