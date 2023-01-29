'''Melhore a versão anterior colocando um parâmetro opcional para definir se o valor de saída será
formatado como moeda ou não. '''

from utilidades import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p), True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p), True)}')
print(f'Aumentando 10% temos, {moeda.moeda(moeda.aumentar(p, 10), True)}')
print(f'Reduzindo 13 %, temos, {moeda.moeda(moeda.diminuir(p, 13), True)}')