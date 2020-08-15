n = float(input('Digite um número qualquer: '))

dob = n * 2 #Dobro do valor recebido
tri = n * 3 #Triplo de n
raiz = n ** (1 / 2) #A raiz quadrada

print(f'O dobro de {n} é {dob}, seu triplo é {tri} e sua raiz quadrada é {raiz:.2f}.')

#É possível obter o mesmo resultado da raiz utilizando a função pow()
#Função pow() executa a mesma função de **(potenciação)

print(f'A raiz de {n} é {pow(n, (1 / 2)):.2f}')
