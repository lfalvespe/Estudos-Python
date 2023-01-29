'''Como remover itens duplicados de lista em Python.

Para remover a duplicidade de elementos em um lista vamos utilizar a função "set()", que tem exatamente esta premissa

Entregar uma lista de dados apenas com valores únicos, o problema é que o retorno de set é um dicionário

Ou seja, teremos uma alteração no tipo de dado, e isso talvez não seja interessante

Então vamos utilizar a função list neste set, que transforma o dicionário em uma lista e aí resolveremos todos os nossos problemas

Veja um exemplo prático da implementação de set:


'''


lista = [1, 1, 2, 3, 3, 4, 5, 5]
print(lista)

lista_unica = list(set(lista))

print(lista_unica) # [1, 2, 3, 4, 5]