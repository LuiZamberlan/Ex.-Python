from random import randint
from time import sleep as sl
#A função sleep() suspende o programa pelo tempo solicitado
from pyfiglet import figlet_format as ff

print(ff('DivinationGame'))
sl(2)

print('=-' * 40)
print('Estou pensando em um número...')
sl(2)
print('Entre 0 e 5..')
sl(2)
print('=-' * 40)
sl(2)
n = randint(0, 5)
#Variável que receberá um valor aleatório(O número que o computador "pensou")

t = int(input('Adivinhe o número: '))

print('Entããããoo....')
sl(4)

if t == n:
    print('Você Ganhou!')
    #Se o número adivinhado for igual ao número sorteado

else:
    print(f'Perdeu! eu pensei no {n}.')
    #Caso o número adivinhado não for o mesmo que o sorteado

print('--FIM--')
