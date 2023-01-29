
n = 0
soma = 0
cont = 0

n = int(input('Digite um número: '))

while n != 999:
  
  soma += n
  cont += 1

  n = int(input('Digite um número: '))

print('Você digitou {} numeros'.format(cont-1))
print('A soma de seus números foi {}'.format(soma))

print('FIM')