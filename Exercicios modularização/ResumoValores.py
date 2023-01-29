'''Adicione ao módulo moeda uma função chamada resumo() que mostre na tela algumas informações geradas pelas
funços que já existem lá.'''

from utilidades import moeda

p = float(input('Digite o preço: R$ '))

moeda.resumo(p, 80, 35)
