'''Quando trabalhamos com listas em Python temos dois métodos que aparentam sem bem parecidos: o append e o extend

Porém eles tem algumas sutis diferenças, o append recebe como parâmetro um iterable

Podemos descrever iterable como um tipo de dado que possui diversos elementos que podem ser iterados, uma lista por exemplo

E com este argumento iterable ele amplia a lista, adicionando os elementos ao fim, vejamos um exemplo:'''

listaA = [1,2,3,4,5]
listaB = [6,7,8]
listaA.extend(listaB)
print(listaA)

'''Desta forma cada um dos elementos da listaB serão adicionados ao fim da listaA, veja o resultado:

[1, 2, 3, 4, 5, 6, 7, 8]'''

'''Por sua vez, o append vai adicionar simplesmente o elemento todo ao final da lista

Independente do tipo de dado ou se for um iterable, veja:'''
print()

listaC = [1,2,3,4,5]
palavraA = 'teste'
listaC.append(palavraA)
print(listaC)
listaD = [99,100]
listaC.append(listaD)
print(listaC)

'''
Veja que mesmo adicionando outro iterable, o Python simplesmente adicionou ele dentro da lista como se fosse outro elemento, conforme o resultado:'''