
r = 'S'
cont = 0
soma = 0

while r in 'Ss': # Mesma coisa se fizer: while r == 'S' 

  n = int(input('Digite um número: '))
  cont += 1
  soma += n
  
  if cont == 1:
    maior = menor = n

  elif n > maior:
    maior = n
    
  elif n < menor:
    menor = n
    

  r = str(input('Quer continuar? ')).upper().strip()[0]

print('Você digitou {} números, a média dos valores foi {}, o maior valor foi {}, o menor valor foi {}.'.format(cont, soma/cont, maior, menor))

print('FIM')
  