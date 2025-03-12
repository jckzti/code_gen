import random

def gerar_numeros():
    # Gere uma lista de 10 números aleatórios entre 1 e 100
    numeros = [random.randint(1, 100) for _ in range(10)]
    
    # Imprima a lista
    print(numeros)

# Execute a função sem precisar passar parâmetro de entrada
gerar_numeros()