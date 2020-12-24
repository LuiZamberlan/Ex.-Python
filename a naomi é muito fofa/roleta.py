from random import randint

list1 = c = e = []


def lnomes(e='',n='',d=''):
    
    if e[0] == 'add':
        n = e[1]
        list1.append(n)
        return f'O nome {list1[-1]} foi adcionado'

    elif e[0] == 'show':
        return list1

    elif e[0] == 'edit':
        d = list1.index(e[1])
        list1[d] = str(input('> '))
        return 'edited'

    elif e[0] == 'delete':
        d = list1.index(e[1])
        del list1[d]
        return 'deleted'

    elif e[0] == 'del_all':
        del list1[:]
        return 'all deleted'

    elif e[0] == 'roll':
        i = randint(0, (len(list1) - 1))
        return list1[i]

    elif e[0] == 'help':
        return 'Options: add; list; edit; delete; del_all; roll; exit'

    elif e[0] == 'exit':
        exit()

    else:
        print('Error 404: command not found, try again..')



while True:
        c = str(input()).lower().strip()
        e = c.split(":")
        print(lnomes(e))
