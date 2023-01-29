'''Crie um programa que calcule a soma de todos os números impares que são múltiplos de 3 no intervalo de 1 a 500 '''

soma = 0

for i in range(1, 501, 2):
  if i % 3 == 0:
    soma +=i

print(soma)

