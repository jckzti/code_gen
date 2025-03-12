# Jogo da Velha!

# Define a matriz do jogo
tabuleiro = [' ' for _ in range(9)]

# Função para imprimir o tabuleiro
def imprime_tabuleiro():
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')

# Função para verificar se alguém ganhou
def verifica_ganho():
    # Linhas
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != ' ':
        return True
    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != ' ':
        return True
    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != ' ':
        return True

    # Colunas
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != ' ':
        return True
    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != ' ':
        return True
    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != ' ':
        return True

    # Diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ':
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' ':
        return True

    # Se ninguém ganhou, retorna False
    return False

# Função para jogar
def jogo_da_velha():
    jogador = 1
    while True:
        imprime_tabuleiro()
        posicao = int(input(f"Jogador {jogador}, insira sua posição (1-9): "))
        if tabuleiro[posicao - 1] != ' ':
            print("Posição já ocupada!")
            continue

        # Marca a posição
        tabuleiro[posicao - 1] = str(jogador)

        # Verifica se alguém ganhou
        if verifica_ganho():
            imprime_tabuleiro()
            print(f"Jogador {jogador} ganhou!")
            break

        jogador = 2 if jogador == 1 else 1

# Inicia o jogo
jogo_da_velha()