# Simulador de Sorte Virtual (Versão 1.0)

import random
import time

def sorteio():
    """Função para realizar o sorteio"""
    print("Sorteando números...")
    time.sleep(2) # Pausa de 2 segundos
    numero_sorteado = random.randint(1, 100) # Gera um número aleatório entre 1 e 100
    return numero_sorteado

def jogo_de_bicho():
    """Função para realizar o jogo de bicho"""
    print("Bem-vindo ao Jogo de Bicho!")
    time.sleep(1)
    print("Você precisa acertar os números sorteados.")
    time.sleep(2)

    sorteio1 = input("Insira o seu primeiro número: ")
    try:
        sorteio1 = int(sorteio1)
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    sorteio2 = input("Insira o seu segundo número: ")
    try:
        sorteio2 = int(sorteio2)
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    numero_sorteado = sorteio()
    if sorteio1 == numero_sorteado or sorteio2 == numero_sorteado:
        print(f"Parabéns! Você acertou o número {numero_sorteado}!")
    else:
        print(f"Lamento, você não acertou o número. O número sorteado foi {numero_sorteado}")

def main():
    """Função principal do programa"""
    jogo_de_bicho()

if __name__ == "__main__":
    main()