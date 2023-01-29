# Usando módulo datetime para pegar a data atual do sistema. 

import datetime

data = datetime.date.today() # Mostra a data completa
dia = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year


print(data)
print(dia)
print(mes)
print(ano)

