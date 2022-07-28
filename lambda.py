def mult(x, y):
    m = x * y
    return m

#Função Lambda: Função anônima que faz o mesmo que a função mult definida acima.

n1 = mult(5, 2)
print(n1)

print()

#Função Lambda:
n2 = lambda x,y: x*y

print(n2(5, 2))