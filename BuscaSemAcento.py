'''No Python temos uma maneira bem interessante e fácil de buscar em uma string ignorando a acentuação

Precisamos utilizar a biblioteca unidecode, e converter as palavras para outro encode

E assim fazer a nossa busca com acentuação ignorada, vamos ver na prática:'''

import unidecode
palavra = "programação"
palavraSemAcentuacao = unidecode.unidecode(palavra)
print(palavraSemAcentuacao)
if(palavraSemAcentuacao.find('cao')):
  print("Encontrado!")