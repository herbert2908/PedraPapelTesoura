from random import randint


def player_interface(opcoes):
    for index, opcao in enumerate(opcoes):
        print(f'{index} = {opcao}')

    input_player = int(input("Qual a sua escolha? "))
    return input_player


def computador_escolha(x):
    computador_opcao = randint(0, len(x) - 1)
    return computador_opcao


def vitoria(escolha, player, computador):
    if player == computador:
        return "Empate"
    elif (player == 0 and computador == len(escolha) - 1) or (
            player > computador and not (player == len(escolha) - 1 and computador == 0)):
        return "Você Venceu!!"
    return "Você Perdeu!!"


def play():
    print('''
    ----------------------
    Pedra, Papel, Tesoura
    Escolha a sua Arma?
    ''')

    # Defina as opções e peça aos competidores para escolher uma
    lista_opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolha_player = player_interface(lista_opcoes)
    escolha_computador = computador_escolha(lista_opcoes)

    # Imprimir as escolhas dos participantes no terminal
    print(f'   Escolha do jogador: {lista_opcoes[escolha_player]}')
    print(f'Escolha do computador: {lista_opcoes[escolha_computador]}')

    # Confeir quem ganhou e imprimir
    resultado = vitoria(lista_opcoes, escolha_player, escolha_computador)
    print(f'\n{resultado}')


def main():
    jogar_denovo = ''
    while jogar_denovo.lower() != 'n':
        play()
        print(f'Você quer jogar de novo?')
        jogar_denovo = input("Digite \'s\' para jogar de novo ou \'n\' para sair: ")


main()