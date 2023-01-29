''' Colocando cores no Terminal
   
   CÓDIGO ANSI:

  \033[style;text;back+m

style:           Text:       Back:
0 - none         30          40
1 - Bold         31          41
4 - Underline    .           .
7 - Negativa     .           .
                 .           .
                 37          47

'''

#EX.:

print('\033[1;31;46m Testando cores com código ANSI \033[m')

#\033[m no finalfoi para não exibir as cores no final do texto

#EX.: Colocando código de cores no "format" do print.

nome = 'Maria'

print('Olá {} {} {}. Bemvinda'.format('\033[33m',nome,'\033[m'))