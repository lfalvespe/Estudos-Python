'''Para gerar um número aleatório podemos utilizar o módulo random e vamos utilizar o método randrange, onde podemos inserir como parâmetro um limite

Ou seja, vamos colocar o número 10 e o número aleatório gerado será até 9!'''


from random import randrange
print(randrange(10))

'''Dessa forma receberemos um float entre 0 e 10 de forma aleatória'''
print()


from random import uniform
print(uniform(0, 10))