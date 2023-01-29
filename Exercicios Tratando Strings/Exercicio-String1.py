""" 1. Crie um programa que leia o nome completo de uma pessoa e exiba:

a) O nome com todas as letras maiúsculas.
b) O nome com todas as letras minúsculas.
c) Quantas letras ao todo sem contar os espaços.
d) Quantas letras tem o primeiro nome.

"""

# Solução:

nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
lista = nome.split()
print(len(lista[0]))