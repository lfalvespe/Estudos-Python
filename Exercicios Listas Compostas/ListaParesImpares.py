'''Crie um programa que leia 7 números e cadastre-os numa lista única que mantenha separados os valores pares e ímpares. No final mostre:

Os valores pares e ímpares em ordem crescente.

'''
numeros = [[], []]

n = 0

for i in range(1, 8):
  n = int(input(f'Digite o {i}° número: '))

  if n % 2 == 0:
    numeros[0].append(n)
  else:
    numeros[1].append(n)

print(f'Os numeros pares foram: {sorted(numeros[0])}')
print(f'Os números ímpares foram: {sorted(numeros[1])}')