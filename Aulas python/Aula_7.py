#Utilizando cores no python utilizando o ANSI escape sequence \033[style;text;backgroundm]
#Style 0(none), 1(bold), 4(underline), 7(negative)
#Text: 30 até 37
#Back: 40 até 47

print(f'\033[0;30;41mOlá\033[m')

print(f'\033[4;33;44mOlá\033[m')

print(f'\033[1;35;43mOlá\033[m')

print(f'\033[0;30;42mOlá\033[m')

print(f'\033[mOlá')

print(f'\033[7;30mOlá\033[m')