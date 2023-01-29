from uteis import numeros
from uteis import texto

# programa principal
titulo = texto.titulo('Testando módulos no Python.')
num = int(input('\033[1;35mDigite um número:\033[0;37m '))
fat = numeros.fatorial(num)
d = numeros.dobro(num)

print(f'\n- \033[1;30;43mO fatorial de {num} é:\033[0;34m {fat}\033[0;37m')
print(f'\n- \033[1;30;43mO dobro de {num} é:\033[0;34m {d}\033[0;37m')