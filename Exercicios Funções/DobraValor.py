def dobra(lista):
  pos = 0
  while pos < len(lista):
    lista[pos] *= 2
    pos += 1

# MainProgram
valores = [2, 4, 8]

dobra(valores)
print(valores)
