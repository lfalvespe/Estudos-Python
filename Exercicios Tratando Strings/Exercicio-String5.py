""" 5. Faça um programa que leia uma frase pelo teclado e diga:

a) Quantas vezes aparece a letra "A".
b) Em que posição ela aparece pela primeira vez.
c) Em que posição ela aparece pela última vez.
"""

frase = str(input('Digite uma frase: ').lower())


print('Quantas letras A na frase {}'.format(frase.count('a')))

print('Primeira letra A na posição {}'.format(frase.find('a')))

print('Última letra A na posição {}'.format(frase.rfind('a')))