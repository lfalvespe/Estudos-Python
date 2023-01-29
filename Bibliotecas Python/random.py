#Biblioteca Ramdom
import random

#Escolher um número aleatoriamente: .random() - Sorteia entre 0 e 1

a = random.random()
print(a)

# .randint(0,4) - Sorteia um inteiro no intervalo indicado

b = random.randint(2, 10)
print(b)

#.choice - Sorteia um número numa lista
lista = [1, 3, 7, 12, 45]

c = random.choice(lista)
print(c)

# .choices(lista, k = int) - Sorteia vários números e cria uma lista de tamanho k (Gera valores repetidos)

numeros = [1, 2, 3, 4, 5]
nomes = ['maria', 'bia', 'leo', 'bel', 'gil']

nom = random.choices(nomes, k=4)
num = random.choices(numeros, k=4)

print(nom)
print(num)

# .sample(lista, k = int) Sorteia vários números e cria uma lista de tamanho k (Gera valores sem repetição)

nom1 = random.sample(nomes, 4)
num1 = random.sample(numeros, 4)

print(nom1)
print(num1)

# .shuffle(lista) - embaralhar uma lista

paises = ['Brazil', 'Canadá', 'Dinamarca', 'EUA', 'França', 'Grécia', 'Holanda']

print(paises)

random.shuffle(paises)
print(paises)
