
T1 = 0
T2 = 1

c = 3

o = int(input('Quer ver quantos elementos da sequencia de FIBONACCI? '))

print(T1, end = ' ')
print(T2, end = ' ')



while c <= o:
  
  T3 = T1 + T2
  print(T3, end = ' ')
  T1 = T2
  T2 = T3
  c += 1