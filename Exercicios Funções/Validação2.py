def leiaInt():
  while True:
    
    n = str(input('Digite um número: ')).strip()
    if n.isnumeric():
      n = int(n)
      print(f'Você digitou o número {n}')
      break
      
    elif n.isalpha():
      print('Você não digitou um número: ')
    else:
      print('Você não digitou um número: ')

# programa principal

leiaInt()


  




