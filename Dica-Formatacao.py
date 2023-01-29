t = ('a', 2, 'b', 6, 'c', 12, 'd', 5.5, 'e', 14.57)

# Formatando Strings
print(f'{" Mostrando Formatação ":#^43}')

# Formatando números:
for n in range(0, len(t)):
  if n % 2 == 0:
    print(f'\nValor de {t[n]:-<25}', end = '')
  else:
    print(f'R$ {t[n]:>6.2f}')
