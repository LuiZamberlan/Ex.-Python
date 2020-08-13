l = float(input('Digite a largura da parede em metros: '))
al = float(input('Digite a altura da parede em metros: '))

#Um litro de tinta pinta 2m², largura * altura da parede obtemos a área dela em m² e dividimos por dois para obter a quantidade de tinta necessária.
lt = (l * al) / 2

print(f'Com uma parede {l}x{al}, você usará {lt:.2f}L de tinta')
