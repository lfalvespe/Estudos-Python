'''Como iterar por duas listas em paralelo com Python 3
Para resolver a situação apenas precisamos utilizar a instrução for de Python, que itera em uma lista normalmente

Então vamos unir as duas listas utilizando a função zip, que faz exatamente isso

Recebemos como retorno uma tupla, com a possibilidade de iterar por ela.

Note que criamos duas listas, representadas pelas variáveis: a e b

Depois iniciamos o for, escolhendo x e y como nomes para os itens de cada iteração sobre as listas

Então aplicamos a função zip nas duas listas, para unir as duas

E é possível imprimir cada um dos itens de forma alternada, como fizemos com print, fácil não?

'''

a = [1, 2, 3]
b = ['a', 'b', 'c']
for x, y in zip(a, b):
    print(x, y) # 1 a, 2 b, 3 c