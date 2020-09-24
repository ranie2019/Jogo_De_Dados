from random import randint

print('-*- ' * 10)
print('         Jogo De Dados')
print('-*- ' * 10)
print('')

print('''Voce Quer Jogar Digite
0 nao
1 sim
''')

jogo = int(input('Digite Sua Escolha: '))

dado = randint(1, 6)

if jogo == 0:
    print('Fim de Jogo')

elif jogo >= 2:
    print('Opção Ivalida')

elif jogo == 1:
    dinheiro = float(input('Digite o valor que Voce quer Depositar R$ '))
    aposta = float(input('Digite o Valor que Voce Vai Apostar R$ '))
    if dinheiro < aposta:
        print('Seu Saldo e Baixo')

    elif dinheiro >= aposta:
        numero = int(input('Digite um Numero De 1 a 6: '))
        if numero >= 7 or numero <= 0:
            print('Opção Ivalida')

        elif dado == numero:
            soma = dinheiro + aposta
            print('')
            print(f'Voce Escolheu {numero} e o Dado Deu {dado} '
                  f'\nVoce Ganhou Seu Saldo e De {soma}')

        elif dado != numero:
            soma = dinheiro - aposta
            print('')
            print(f'Voce Escolheu {numero} e o Dado Deu {dado} '
                  f'\nVoce Perdeu Seu Saldo e De {soma}')
    saldop = dinheiro + aposta
    saldon = dinheiro - aposta
    while jogo == 1:
        print('')
        print('''Voce Quer Jogar Mais Digite
0 nao
1 sim
''')
        jogo = int(input('Digite Sua Escolha: '))
        if jogo == 0:
            print('Fim de Jogo')

        elif jogo >= 2:
            print('Opção Ivalida')

        elif jogo == 1:
            aposta = float(input('Digite o Valor que Voce Vai Apostar R$ '))
            if dinheiro < aposta:
                print('Seu Saldo e Baixo')
            elif dinheiro > aposta:
                numero = int(input('Digite um Numero De 1 a 6: '))
                if numero >= 7 or numero <= 0:
                    print('Opção Ivalida')

                elif dado == numero:
                    soma = dinheiro + aposta
                    print('')
                    print(f'Voce Escolheu {numero} e o Dado Deu {dado} '
                          f'\nVoce Ganhou Seu Saldo e De {soma}')

                elif dado != numero:
                    soma = dinheiro - aposta
                    print('')
                    print(f'Voce Escolheu {numero} e o Dado Deu {dado} '
                          f'\nVoce Perdeu Seu Saldo e De {soma}')
