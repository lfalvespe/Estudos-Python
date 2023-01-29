'''Esta é uma dúvida que assola muitos programadores, mas felizmente há uma solução simples.

Geralmente o programador precisa alterar os dados de uma tupla, então a conversão para um dicionário é muito indicada

Já que, teoricamente, não podemos mudar dados de uma tupla'''


tupla = (('valor', 'chave'),(16, 'numero'),(True, 'verdadeiro'))
dicionario = dict((y, x) for x, y in tupla)
print(dicionario) # {'chave': 'valor', 'numero': 16, 'verdadeiro': True}