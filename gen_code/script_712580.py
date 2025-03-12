import random
import time

# Código do teste aqui

class JogoDaForca:
    def __init__(self):
        self.palavras = ["banana", "maçã", "pêra", "laranja"]
        self.escolhida = random.choice(self.palavras)
        self.tentativas = 6
        self.letras_acertadas = ["_"] * len(self.escolhida)

    def imprimir_estado_jogo(self):
        print(" ".join(self.letras_acertadas))

    def jogar(self):
        while True:
            self.imprimir_estado_jogo()
            chute = input("Chute uma letra: ").lower()

            if len(chute) != 1:
                print("Por favor, chute apenas uma letra!")
                continue

            if chute in self.escolhida:
                for i in range(len(self.escolhida)):
                    if self.escolhida[i] == chute:
                        self.letras_acertadas[i] = chute
            else:
                self.tentativas -= 1
                print(f"Você errou! Você tem {self.tentativas} tentativas restantes.")

            if "_" not in self.letras_acertadas:
                print("Parabéns, você ganhou!")
                break

            time.sleep(0.5)

        play_again = input("Quer jogar novamente? (s/n): ").lower()
        if play_again == "s":
            self.__init__()
            self.jogar()

if __name__ == "__main__":
    jogo = JogoDaForca()
    jogo.jogar()