''' Crie um programa que leia um número e diga se ele é ou não um número PRIMO'''

n = int(input('Digite um número: '))

primos = 0
divisores = 0

for i in range(1, n+1):
    if n % i == 0:
        divisores += 1

if divisores == 2:
    print('{} é Primo'.format(n))
else:
    print('{} não é Primo!'.format(n))
