# Recebe uma cadeia de caracteres do usuário e guarda na variável frase
frase = str(input('Digite uma frase: ')).strip()

print('Sua frase em maiúscula é {}:'.format(frase.upper()))
print('Sua frase em minúsculas é {}'.format(frase.lower()))
print('Se usar capitalize fica {}:'.format(frase.capitalize()))
print('Se usar title fica {}:'.format(frase.title()))

print('\n')

# Mostrar a letra da posição 9 (Começa em 0 e mostra até a 8)
print(frase[9])

# Mostrar da posição 0 até a posição 11 (Vai do 0 até o 10)
print(frase[0:11])

# Mostrar da posição 4 até a posição 12
print(frase[4:13])

# Mostrar até a posição 13
print(frase[:14])

# Mostrar da posição 5 até o final
print(frase[5:])

# Mostrar um intervalo pulando de 2 em duas casas
print(frase[6:11:2])

# Mostrar um intervalo da posição 7 até o final pulando de 3 em 3.
print(frase[7::3])

# Mostrar o tamanho da String
print(len(frase))

# Contar ocorrência de caracteres na string
print(frase.count('o'))

# Contar ocorrência de caracteres da posição 0 até a posição 6
print(frase.count('o', 0, 7))

#  Procurar algo na string (mostra a posição onde inicia)
print(frase.find('acte'))

# Verificar se existe algo dentro da string: Operador "in" mostra True ou False
print('python' in frase)

# Mostrar tudo em maiúscula
print(frase.upper())

# Mostrar tudo em minúscula
print(frase.lower())

# Substituir algo na string
print(frase.replace('python', 'javascript'))

# Mostrando só a primeira letra da frase em maiúscula
print(frase.capitalize())

# Mostrando a primeira letra de cada palavra em maiúscula
print(frase.title())

# Remover espaços indesejáveis no início e no final da string.
print(frase.strip())

# Dividir a string e criar uma lista com as palavras
print(frase.split())

# Mostra o elemento 1 na lista criada com o split
print(frase.split()[1])

# junta palavras da lista com um simbolo
print(('_'.join(frase.split())))