def metade(p):
   pn = p/2
   return pn
def dobro(p):
    pn = 2*p
    return pn
def aumentar(p, t):
    pn = p + (t/100)*p
    return pn
def diminuir(p, t):
    pn = p - (t/100)*p
    return pn

def moeda(p, show=False):
    if show:
        return f'R$ {p}'
    else:
        return p
def resumo(p, a, d):
    print('-'*30)
    print('    Resumo do valor')
    print('-'*30)

    print(f'{"Preço analizado:":<25} {moeda(p, True):>8}')
    print(f'{"Dobro do preço:":<25} {moeda(dobro(p), True):>8}')
    print(f'{"Metade do preço:":<25} {moeda(metade(p), True):>8}')
    print(f'{"Preço aumentado"} {a}% {":":<5} {moeda(aumentar(p, a), True):>8}')
    print(f'{"Preço diminuído"} {d}% {":":<5} {moeda(diminuir(p, d), True):>8}')

