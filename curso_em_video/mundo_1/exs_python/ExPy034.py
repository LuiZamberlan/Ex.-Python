s = float(input('Valor do salário: R$'))

if s > 1250:
    print(f'Você recebeu aumento de 10% R${(s / 10) + s:.2f}')

else:
    print(f'Você recebeu aumento de 15% R${((s * 15) / 100) + s:.2f} ')
