s = float(input('Quanto você ganha de salário? R$'))

#O salário é somado com 15% do mesmo, para calcular o aumento
aum = s + ((s * 15) / 100)

print(f'Com seu aumento de 15%, você agora recebe R${aum:.2f} / mês.')
