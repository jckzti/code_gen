import random

def sorteia_numero(minimo, maximo):
    """Sortea um número aleatório entre minimo e maximo."""
    return random.randint(minimo, maximo)

def jogo_da_sorte():
    """Jogo da Sorte: o usuário escolhe um número secreto e o programa tenta adivinhá-lo."""
    print("Bem-vindo ao Jogo da Sorte!")
    
    # Pedir para o usuário escolher um número secreto
    numero_secreto = int(input("Escolha um número secreto entre 1 e 100: "))
    
    # Tentar adivinhar o número secreto com tentativas limitadas (10)
    tentativas = 0
    while tentativas < 10:
        chute = sorteia_numero(1, 100)
        
        print(f"Tentativa {tentativas+1}: O programa chuta... {chute}")
        
        if chute == numero_secreto:
            print("Parabéns! O programa adivinhou o número secreto!")
            return
        elif chute < numero_secreto:
            print("O número que eu chutei é menor que o número secreto. Tente novamente!")
        else:
            print("O número que eu chutei é maior do que o número secreto. Tente novamente!")
        
        tentativas += 1
    
    # Se o programa não adivinhar o número em 10 tentativas, informar ao usuário
    print(f"Desculpe! O programa não conseguiu adivinhar o número secreto (ou você é muito esperto!). O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_da_sorte()