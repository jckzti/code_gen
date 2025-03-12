# Script "Mistério da Velha Casa Abandonada"

import random

def velha_casa_abandonada():
    # Crie uma história aleatória
    historias = [
        "Você encontrou uma velha casa abandonada na floresta. A porta estava trancada, mas você conseguiu encontrar uma janela aberta.",
        "Ao entrar na casa, você viu um quarto com móveis antigos e cobertos de poeira. Súbito, você ouviu um barulho vindo do andar superior.",
        "Você descobriu que a casa pertencia a uma família rica há muitos anos. Agora, ela está em ruínas e cheia de segredos.",
    ]

    # Escolha uma história aleatória
    historia_escolhida = random.choice(historias)

    # Mostre a história ao usuário
    print("Aqui está o que aconteceu:")
    print(historia_escolhida)
    print()

    # Dê um final aleatório à história
    finais = [
        "Mas você não conseguiu encontrar nenhuma pista sobre quem fez isso.",
        "E, de repente, a porta se fechou sozinha e você ficou preso!",
        "E descobriu que era uma armadilha para proteger um tesouro secreto."
    ]

    # Escolha um final aleatório
    final_escolhido = random.choice(finais)

    # Mostre o final à história ao usuário
    print("E assim, a história terminou:")
    print(final_escolhido)

# Execute a função principal
velha_casa_abandonada()