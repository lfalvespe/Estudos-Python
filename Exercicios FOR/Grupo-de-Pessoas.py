''' Crie um programa que leia nome idade e sexo de 4 pessoa e no final mostre:

- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos

'''

soma_idades = 0
idade_hmv = 0
mulheres_20 = 0

for i in range(1, 5):
    nome = str(input('Digite o nome da {}a pessoa: '.format(i))).title().strip()
    idade = int(input('Digite a idade do(a) {}: '.format(nome)))
    sexo = str(input('Digite o sexo do(a) {} (M/F): '.format(nome))).upper().strip()
    soma_idades += idade

    if sexo == 'M' and idade > idade_hmv:
        idade_hmv = idade
        nome_hmv = nome

    elif sexo == 'F' and idade < 20:
        mulheres_20 += 1


media = soma_idades/4

print('- A média de idade do grupo é {:.0f}'.format(media))
print('- O home mais velho é {}'.format(nome_hmv))
print('- Ao todo foram {} mulheres abaixo de 20 anos.'.format(mulheres_20))


