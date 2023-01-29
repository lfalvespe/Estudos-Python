''' Crie um programa que leia a idade de 7 pessoas e diga quantas delas já atingiram a maioridade.
Considere 21 anos. '''

maiores = 0

for i in range(1, 8):
    idade = int(input('Digite a idade da {}a pessoa: '.format(i)))

    if idade >= 21:
        maiores += 1

print('Ao todo você digitou {} maiores de idade.'.format(maiores))