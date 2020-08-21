n = str(input('Nome completo: ')).strip().lower()

print(f'Seu primeiro nome é {n.split()[0].capitalize()} e seu ultimo é {n.split()[-1].capitalize()}')
#O index -1 de n.split() permite pegar o último item da lista sem precisar saber o número total de itens

#Exemplo da Aula:

nome = n.split()

print(f'Seu primeiro nome é {nome[0]} e seu ultimo é {nome[len(nome)-1]}')
#O método len() mostra o total de itens na lista criada com n.split(), logo depois, é subtraido por 1 para obter o index do último item(o ultimo nome da variável 'n')
