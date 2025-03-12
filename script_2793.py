# Caça ao Tesouro!

# Defina o nome do jogador
nome_jogador = input("Qual é o seu nome? ")

# Defina o número de clusas para encontrar
n_clusas = 5

# Defina as coordenadas das clusas (para este exemplo, vamos usar números aleatórios)
import random
clusas = []
for i in range(n_clusas):
    clusa_x = random.randint(1, 10)
    clusa_y = random.randint(1, 10)
    clusas.append((clusa_x, clusa_y))

# Defina o tamanho do mapa (para este exemplo, vamos usar um mapa de 10x10)
tamanho_mapa = 10

# Imprima o mapa com as coordenadas das clusas
print("  ", end="")
for i in range(tamanho_mapa):
    print(i, end=" ")
print()
for i in range(tamanho_mapa):
    print(i, end=" ")
    for j in range(tamanho_mapa):
        if (i+1, j+1) in clusas:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()

# Faça o jogador encontrar as clusas
while True:
    # Peça ao jogador para digitar as coordenadas da clusa que deseja encontrar
    x = int(input("Digite a coordenada X da clusa: "))
    y = int(input("Digite a coordenada Y da clusa: "))

    # Verifique se as coordenadas estão dentro do mapa e se é uma clusa válida
    if 1 <= x <= tamanho_mapa and 1 <= y <= tamanho_mapa:
        if (x, y) in clusas:
            print("Você encontrou uma clusa!")
            clusas.remove((x, y))
        else:
            print("Essa clusa não existe ou você errou as coordenadas.")
    else:
        print("Coordenadas inválidas. Tente novamente.")

    # Verifique se todas as clusas foram encontradas
    if not clusas:
        print(f"Parabéns, {nome_jogador}! Você encontrou todas as clusas!")
        break

# Fim do jogo
print("Fim de jogo. Obrigado por jogar!")