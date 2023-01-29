
def ajuda(com):
  titulo(f'Acessando Menu do comando "{com}"', 4)
  print(c[6], end='')
  help(com)
  print(c[0])


c = ('\033[m',         # 0 - Sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 3 - Amarelo
     '\033[0;30;44m',  # 4 - Ciano
     '\033[0;30;45m',  # 5 - Roxo
     '\033[0;30;47m'   # 6 - Branco
     
);

def titulo(msg, cor=0):
  tam = len(msg) + 4
  print(c[cor], end='')
  print('*'*tam)
  print(f'  {msg:^}  ')
  print('*'*tam)
  print(c[0])


# Programa Principal
titulo('Sistema de Ajuda Pyhelp', 1)

while True:
  comando = (str(input(f'{c[3]}Digite um comando{c[0]}: ').strip().lower())) 
  if comando ==  'fim':
    print(f'{c[2]}VOLTE SEMPRE!!!{c[0]}')
    break
  else:
    ajuda(comando)

    

