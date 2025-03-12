# Importando biblioteca para números aleatórios
import random

# Função para verificar se um número é par ou ímpar
def eh_par(num):
    return num % 2 == 0

# Variável para armazenar o resultado da média
media = 0

# Gerando números aleatórios e verificando a paridade
for _ in range(10): # 10 iterações, você pode mudar isso
    num_aleatorio = random.randint(1, 100)
    if eh_par(num_aleatorio):
        print(f"O número {num_aleatorio} é par.")
    else:
        print(f"O número {num_aleatorio} é ímpar.")

    # Calcular a média
    media += num_aleatorio

# Após as iterações, calcular e imprimir a média dos números gerados
media /= 10 # Divisão por 10 para obter a média
print(f"Média dos números gerados: {media:.2f}") # Formatação da saída com duas casas decimais