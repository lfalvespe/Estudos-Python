""" Crie um programa que leia o nome completo de uma pessoa e mostre

a) O primeiro nome.
b) O último nome.
"""

nome = str(input('Digite o seu nome completo: '))

print('Seu primeiro nome é: {}'.format(nome[0:nome.find(' ')]))

print('Seu último nome é: {}'.format(nome[nome.rfind(' ')+1:]))