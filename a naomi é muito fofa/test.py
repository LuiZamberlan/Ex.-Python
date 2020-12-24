from random import randint

list = []

n = str(input('Adcione um nome a lista- '))
list.append(n)
while True:
    a = str(input('Gostaria de adcionar mais um nome?[Y/N] ')).upper().strip()
    
    if a == 'Y':
        n = str(input('Nome - '))
        list.append(n)
        
    elif a == 'N':
        while True:
            f = int(input("""
                [0] Roll
                [1] Add
                [2] Rm
                [3] Edit
                [4] Rm all
                [5] Quit

            >>> """))
            if f == 0:
                al = randint(0, len(list)-1)
                print(list[al])
                
            elif f == 1:
                n = str(input('Adcione um nome a lista- '))
                list.append(n)
                
            elif f == 2:
                print('Qual vc quer excluir?')
                h = 0
                for i in list:
                    print(f'[{i}] -> {h}')
                    h += 1
                    
                print("cancelar = 999")
                
                while True:
                    i = int(input(">>> "))

                    if i == 999:
                        print("cancelado")
                        break
                    
                    elif i > len(list) or i < 0:
                        print("Error 404: command not found")
                        
                    else:
                        del list[i]
                        break

            elif f == 3:
                print("Qual nome você deseja editar? ")
                h = 0
                for i in list:
                    print(f'[{i}] -> {h}')
                    h += 1

                print("cancelar = 999")
                while True:
                    i = int(input(">>> "))

                    if i == 999:
                        print("cancelado")
                        break
                    
                    elif i > len(list) or i < 0:
                        print("Error 404: command not found")
                        
                    else:
                        j = str(input("Qual nome quer colocar no lugar? "))
                        list[i] = j
                        break
                
            elif f == 4:    
                del list[:]
            
            elif f == 5:
                g = str(input('Are you sure?[Y/N] ')).upper().strip()
                
                if g == "Y":
                    exit()
                    
                elif g == "N":
                    pass
                
                else:
                    print("Error 404: command not found")
            else:
                print('Error 404: command not found')

    else:
        print('Error 404: command not found')

print('End')

