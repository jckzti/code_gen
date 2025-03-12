# Script para gerar uma lista de números primos

def eh_primo(num):
    """Verifica se o número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def gerar_primos(max_num):
    """Gera uma lista de números primos até o número máximo."""
    primos = []
    for num in range(2, max_num + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

# Solicita ao usuário o número máximo
max_num = int(input("Digite o número máximo: "))

# Gera a lista de números primos
primos = gerar_primos(max_num)

# Imprime a lista de números primos
print(f"Números primos até {max_num}:")
for primo in primos:
    print(primo)