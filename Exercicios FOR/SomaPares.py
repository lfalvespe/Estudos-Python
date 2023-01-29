''' Crie um programa que leia 6 números inteiros e mostre a soma apenas dos que forem pares'''

soma = 0

for i in range(1, 7):
  n = int(input('Digite o {}º número: '.format(i)))

  if n % 2 == 0:
    soma +=n

print(soma)
  
  