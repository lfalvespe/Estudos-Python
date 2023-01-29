'''
Para remover um elemento de uma lista podemos utilizar o método remove de Python, diretamente na lista

Ele leva como argumento um valor, e remove a primeira ocorrência ao encontrá-la.

Ou seja, podemos então excluir um elemento de uma lista por meio do valor dele'''

my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.remove(4)
print(my_list) # [1, 2, 3, 5]