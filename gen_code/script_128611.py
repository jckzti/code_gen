import random

# Escolhendo um número aleatório entre 1 e 100 (inclusive) para o jogador ter que adivinhar
numero_secreto = random.randint(1, 100)

# Inicializando o número de tentativas do jogador
tentativas = 0

print("Bem-vindo ao jogo de adivinhação de números!")
print("O objetivo é encontrar o número secreto entre 1 e 100.")

while True:
    # Pedindo para o usuário digitar seu chute (número)
    chute = input("Diga um número: ")

    # Verificando se o usuário digitou um número válido
    if not chute.isdigit():
        print("Você precisa digitar um número!")
        continue

    # Converte o chute para um número inteiro
    chute = int(chute)

    # Incrementa o número de tentativas
    tentativas += 1

    # Verifica se o chute está dentro do intervalo permitido (entre 1 e 100)
    if chute < 1 or chute > 100:
        print("Você precisa digitar um número entre 1 e 100.")
        continue

    # Se o chute for igual ao número secreto, parar a execução
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
        break
    elif chute < numero_secreto:
        print("Muito baixo. Tente novamente.")
    else:
        print("Muito alto. Tente novamente.")