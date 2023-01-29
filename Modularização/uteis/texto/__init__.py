def titulo(msg):
  tam = len(msg)+4
  print('='*tam)
  print('\033[1;30;46m')
  print(f'{msg:^{tam}}')
  print('\033[0;37m')
  print('='*tam)
  print('\033[0;37m')