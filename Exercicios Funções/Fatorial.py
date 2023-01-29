# Fatorial

def fatorial(n = 1):
  fat = 1
  c = n
  
  while c > 0:
    fat *= c
    c -= 1
  return fat

f = fatorial(4)
print(f)
