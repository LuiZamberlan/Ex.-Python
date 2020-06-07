da = input('Digite algo: ')
#Váriavel que irá registrar um texto qualquer e como o tipo não está especificado ele vai registrar um texto tipo string.

print(f'O tipo primitivo desse valor é {type(da)}')
#Função Type(): Ela exibe o tipo de um valor ou variável. O valor ou variável, que é chamado de argumento da função, tem que vir entre parênteses.

print(f'Só tem espaços? {da.isspace()}')
#Verifica se tem espaços.

print(f'É um número? {da.isnumeric()}')
#Verifica se tem somente números.

print(f'É alfabético? {da.isalpha()}')
#Verifica se tem somente letras.

print(f'É alfanumérico? {da.isalnum()}')
#Verifica se tem números e letras ao mesmo tempo.

print(f'É capitalizado? {da.istitle()}')
#Verifica se o texto está capitalizado(Começando com uma letra maiúscula e o restante em minúsculas.).

print(f'Está em maiúsculas? {da.isupper()}')
#Verifica se o texto está em maiúsculas.

print(f'Está em minúsculas? {da.islower()}')
#Verifica se o texto está em minúsculas.
