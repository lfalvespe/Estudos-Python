''' Crie um programa que peça leia um número e pergunte ao usuário para qual base ele quer converter:

1 para binário
2 para octal
3 para hexadecimal

'''

n = int(input('Digite um número: '))

print('''
Para qual base quer converter? 

[1] Binário
[2] Octal
[3] Hexadecimal
               ''')

escolha = int(input('Escolha uma opção: '))

if escolha == 1:
  print('''
{} no sistema binário é {}'''.format(n, bin(n)[2:]))
elif escolha == 2:
  print('''
{} em Octal é {}'''.format(n, oct(n)[2:]))
elif escolha == 3:
  print('''
{} em Hexadecimal é {}'''.format(n, hex(n)[2:]))
else:
  print('''
        Opção inválida''')
