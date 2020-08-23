k = float(input('Qual a distância da viagem? '))

if k <= 200:
    print(f'O preço da passagem é de R${k * 0.50:.2f}')
    #O preço para viagens curtas o custo é de R$0,50 por km.

else:
    print(f'O preço da passagem é de R${k * 0.45:.2f}')
    #Para viagens mais longas o custo é de R$0,45 por km.

#ou->

d = k * 0.50 if k <= 200 else k * 0.45
print(f'O preço da viagem é de R${d:.2f}')
