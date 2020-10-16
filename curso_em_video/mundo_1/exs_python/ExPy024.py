c = str(input('Digite o nome da sua cidade: ')).lower().strip()
#'c' recebe o nome da cidade que são colocadas em letras minúsculas e logo depois é retirado os espaços desnecessários no começo e no fim da cadeia de caracteres

print(f'Sua cidade tem "Santo" no nome? {"santo" in c}')
#O operador 'in' verifica se tem "santo" em 'c'

#ou->

print(f'Sua cidade tem "Santo" no nome? {c[:5] == "santo"}')
#Utilizamos o index para localizar o "santo" na cadeia de caracteres
