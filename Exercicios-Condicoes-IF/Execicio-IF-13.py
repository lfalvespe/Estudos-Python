''' Escreva um programa que leia duas notas de um aluno, calcule sua média e mostra:

- Média abaixo de 5.0 (Reprovado)
- Média entre 5.0 e 6.9 (Recuperação)
- Média 7.0 ou superior (Aprovado)

'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

if media < 5.0:
  print('Média {}: REPOVADO'.format(media))

elif media >= 5 and media <= 6.9:
  print('Média {}: RECUPERAÇÃO'.format(media))

else:
  print('Média {}: APROVADO'.format(media))



