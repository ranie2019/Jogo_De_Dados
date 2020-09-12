from random import randint

print('Voce Deve advinhar o Numero de 1 a 5')

numero = int(input('Digite o Numero desejado: '))
dados = randint(1, 5)

if numero > dados:
    print('*' * 22)
    print(f'O Seu Numero e Mais Alto {dados}')
    print('*' * 22)

elif numero < dados:
    print('*' * 22)
    print(f'O Seu Numero e Mais Baixo {dados}')
    print('*' * 22)

elif numero == dados:
    print(f'Parabens Voce Acertou {dados}')

else:
    print('Voce e Burro Numero Errado')
