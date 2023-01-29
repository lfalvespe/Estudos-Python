def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'ERRO: "{(entrada)}" é um preço inválido')
        else:
            valido = True
            return float(entrada)
