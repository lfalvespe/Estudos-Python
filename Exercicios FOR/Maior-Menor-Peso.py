''' Crie um programa que leia o peso de cinco pessoa e diga qual o maior e o menor peso'''


peso = float(input('Digite o peso da 1a pessoa: '))
maior = menor = peso

for i in range(2, 6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(i)))

    if peso > maior:
        maior = peso

    elif peso < menor:
        menor = peso

print('O maior peso foi: {} Kg\nO menor peso foi {} kg'.format(maior,menor))







