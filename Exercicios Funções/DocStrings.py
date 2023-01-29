def mediarit(a, b, c):
  '''
  * Calcula a média aritmética entre 3 números reais *
  - a, b, c: números reais
  - retorno: média

  Autor: Fernando Alves
  ''' 
  

  m = (a+b+c)/3
  return(m)

  
media = mediarit(2, 4, 8)
print(f'{media:.2f}')

help(mediarit)
