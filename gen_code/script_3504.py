import random

def gerar_numero_aleatorio():
    """Gera um número aleatório entre 1 e 100."""
    return random.randint(1, 100)

# Gere dois números aleatórios
numero1 = gerar_numero_aleatorio()
numero2 = gerar_numero_aleatorio()

# Calcule a soma dos números
soma = numero1 + numero2

print(f"O número {numero1} mais o número {numero2} é igual a {soma}.")