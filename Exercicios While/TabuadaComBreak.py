
c = 1

while True:
  n = int(input('Quer ver a tabuada de qual número? '))

  if n < 0:
    break
  
  else: 
    while c <= 10:
      
      print(f'{n} x {c} = {n*c}')
      c +=1
  

  c = 1

print('FIM DA EXECUÇÃO')