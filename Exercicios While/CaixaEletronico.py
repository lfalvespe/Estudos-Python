''' Crie um programa que simule o funcuonamento de um caixa eletrônico. Pergunte o valor (inteiro) a ser sacado e em seguida o programa indica quantas cédulas de cada valor (R$ 50, R$ 20, R$ 10, R$ 1) serão entregues'''

n = int(input('Qual o valor inteiro a ser sacado? '))

c50 = n//50
c20 = (n%50)//20
c10 = ((n%50)%20)//10
c1 = ((n%50)%20)%10



if n % 50 == 0:
  print (f'Total de cédulas de R$ 50,0: {n//50}')
elif (n % 50) % 20 == 0:
  if c50 != 0:
    print (f'Total de cédulas de R$ 50,0: {n//50}')
  print(f'Total de cédulas de R$ 20,0: {(n%50)//20}')

elif ((n % 50)%20)%10 == 0:
  if c50 != 0:
    print (f'Total de cédulas de R$ 50,0: {c50}')
  if c20 != 0:
    print(f'Total de cédulas de R$ 20,0: {c20}')
  
  print(f'Total de cédulas de R$ 10,0: {c10}')

else:

  if c50 != 0: 
    print (f'Total de cédulas de R$ 50,0: {n//50}')
  if c20 != 0:
    print(f'Total de cédulas de R$ 20,0: {(n%50)//20}')
  if c10 != 0:
    print(f'Total de cédulas de R$ 10,0: {((n%50)%20)//10}')
  print(f'Total de cédulas de R$ 1,0: {c1}')

