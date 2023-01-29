r = o = 0
maior = 0

n1 = int(input('Digite o 1o valor: '))
n2 = int(input('Digite o 2o valor: '))

while r != 5:

    print('''

  [1] - SOMAR
  [2] - Multiplicar
  [3] - Maior
  [4] - Novos números
  [5] - Encerrar        
  ''')

    o = int(input('Escolha uma opção: '))

    if o == 1:
        print('A soma de {} com {} vale {}: '.format(n1, n2, n1 + n2))

    elif o == 2:
        print('{} multiplicado por {} é: {}'.format(n1, n2, n1 * n2))

    elif o == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2

        print('O maior valor digitado foi {}'.format(maior))

    elif o == 4:
        n1 = int(input('Digite o 1o valor: '))
        n2 = int(input('Digite o 2o valor: '))

    elif o == 5:
        r = 5

    else:
        print('Opção inválida, Tente novamente!')

    if n2 > maior:
        maior = n2

print('Fim do programa!!!')