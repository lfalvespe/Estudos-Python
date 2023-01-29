'''Como remover chave de dicionário em Python

Para remover uma chave de um dicionário utilizamos duas formas, a primeira é com o método pop

Nele vamos passar a chave que precisa ser removida e também um segundo argumento como None

'''

dict = {'name': 'Matheus', 'age': 30}
print(dict)
dict.pop('name', None)
print(dict) # {'age': 30}

'''A outra forma é com a instrução del. Implementamos o del no nosso dicionário e a chave age foi removida

'''
print()

dict1 = {'name': 'Helen', 'city': 'Recife'}
print(dict1)

del dict1['name']
print(dict1) # {}
