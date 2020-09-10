from random import randint

print('''Voce Deseja jogar dados
1 - sim
2 - nao
''')
numero = int(input('Digite o Numero desejado: '))
if numero == 1:
    dados = randint(1, 6)
    print('*' * 22)
    print(f'O Valor Do Dado Foi: {dados}')
    print('*' * 22)
    while numero == 1:
        print('''Voce Deseja jogar De Novo
1 - sim
2 - nao
        ''')
        numero = int(input('Digite o Numero desejado: '))
        if numero == 1:
            dados = randint(1, 6)
            print('*' * 22)
            print(f'O Valor do Dado Foi {dados}')
            print('*' * 22)
        elif numero == 2:
            print('Obrigado')
        else:
            print('Voce e Burro Numero Errado')
elif numero == 2:
    print('Obrigado')
else:
    print('Voce e Burro Numero Errado')
