# Escopo de variáveis

def teste():
  y = 8
  n1 = 14

  global n2
  n2 = 20
  
  print(f'N1 na função teste vale {n1}')
  print(f'\nNa função teste x vale {x}')
  print(f'Na função teste y vale {y}')

 
# Programa principal.

x = 4
n1 = 7

n2 = 10


print(f'N1 no programa principal vale {n1}')
# Vai exibir o valor de n1 = 7 fora e n1 = 14 dentro da função.


teste()

print(f'\nN2 no programa principal valia 10 mas foi alterada para {n2} pois dentro da função teste foi declarada e marcada como global.')


print(f'\nNo programa principal x vale {x}')
# Exibe corretamente pois a variável x foi definida dentro do programa principal (esopo global)

print('\nAqui embaixo dá erro pois y foi definida dentro da função teste(), ou seja, tem escopo local.')

print(f'No programa principal y vale {y}')
# Vai dar erro pois a variável y foi definida dentro da funçaõ teste (), Ou seja, tem escopo local.



