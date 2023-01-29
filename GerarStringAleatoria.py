# como gerar string com letras e números aleatórios em Python


import string
import random
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))
print(random_generator()) # M4ICUV
print(random_generator()) # 76QUM7


'''Para criar esta string aleatória vamos utilizar dois módulos:

string;
random;
Então primeiramente vamos importá-los no nosso código

Depois vamos criar uma função para resolver nosso problema, esta função receberá como argumento o tamanho da string aleatória que precisamos retornar

Na função teremos um for que vai gerar os dígitos aleatórios pela quantidade que passamos pelos argumentos

Veja a função que resolve o problema:

import string
import random
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))
print(random_generator()) # M4ICUV
print(random_generator()) # 76QUM7
Veja que os textos foram gerados com 6 caracteres, que é exatamente o que colocamos como parâmetro default da nossa função

Com o random.choice resgatamos um caractere aleatório

E por fim temos o método join, que é utilizado para unir a nossa string

A última instrução de nossa função é retornar o que foi gerado aleatóriamente pelo código de Python'''