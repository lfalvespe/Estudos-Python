''' Crie um programa que leia uma frase e diga se ela é ou não um PALÍNDROMO
(Desconsiderando os espaços).

'''

frase = str(input('Digite uma frase: ')).lower().strip().replace(' ', '')

print(frase)

ifrase = frase[::-1]
print(ifrase)

if frase == ifrase:
    print('Sua frase é um Palíndromo!')
else:
    print('Sua frase não é um Palíndromo!')

''' Exemplos:

- Apos a sopa
- A sacada da casa
- A torre da derrota
- O lobo ama o bolo
- Anotaram a data da maratona

'''



