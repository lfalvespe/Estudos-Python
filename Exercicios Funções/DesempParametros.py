'''Desempacotando parâmetros:
 Cria uma tupla com todos os valores passados como 
 parâmetro:'''

def contador(*num):   
  print(f'Recebi {len(num)} valores, cuja soma vale {sum(num)}')

contador(1, 8, 13, 25)
contador(2, 1, 5)
contador(7)



