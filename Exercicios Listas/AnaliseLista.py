'''Crie um programa que leia vários valores e adicione numa lista. Ao final informe:

a) Quantos valores foram digitados.
b) A lista de valores em ordem decrescente.
c) Se o valor 5 faz parte da lista.

'''
lista = []
  

while True:
  lista.append(int(input('Digite um valor: ')))
  o = str(input('Quer continuar? [S/N] '))
  if o in 'Nn':
    break

print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Valores em ordem decrescente: {lista})
print('5 Faz parte da lista.' if 5 in lista else '5 não faz parte da lista')