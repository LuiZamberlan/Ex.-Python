f = str(input('Digite uma frase: ')).strip().lower()

print(f'Quantas vezes aparece a letra "a"? {f.count("a")}')
#O método count() contará quantos 'a's tem na string

print(f'Qual foi a 1° vez que apareceu? Na {f.find("a") + 1}° Posição')
#O método find() indicará qual o index do 1° 'a' na string

print(f'Qual foi a ultima vez que apareceu? Na {f.rfind("a") + 1}° Posição')
#O método rfind() executa o mesmo comando do find(), mas começando pela direita
