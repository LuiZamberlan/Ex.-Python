m = float(input('Digite um valor em metros: '))

#Conversão de metros para kilometros, hectrometro, decâmetro e decimetro.(desafio)
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
#Conversão de metros para centímetros e milímetros(exercício)
cm = m * 100
mm = m * 1000

print(f'{m} metros em centímetros é {cm:.1f}..')
print(f'{m} metros em milímetros é {mm:.1f}.')

print(f'{m} metros em decímetros é {dm:.1f}.')
print(f'{m} metros em decâmetros é {dam:.2f}.')
print(f'{m} metros em hectometros é {hm:.2f}.')
print(f'{m} metros em kilometros é {km:.3f}.')
