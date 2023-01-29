""" Crie um programa que leia o nome completo de uma pessoa e diga se ela tem "SILVA" no nome. """

nome = str(input('Digite seu nome completo: ')).lower().strip()


print('Tem SILVA no nome: {}'.format('silva' in nome))
