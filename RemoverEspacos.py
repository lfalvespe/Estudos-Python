''' Remover Espaços de uma string'''

frase = '   Eu estudo Python         '

frase.strip() # Remove os espaços no início e no final da string

frase.lstrip() # Remove os espaços à esquerda
frase.rstrip() # Remove os espaços à direita

# Para substituir os espaços entre as palavras:
frase = 'Eu estudo Python'

frase.replace(' ', '')

print(frase)

# Saída: EuestudoPython
