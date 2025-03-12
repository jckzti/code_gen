import random

# Dicionário com nomes e idades
nomes = {
    "João": 25,
    "Maria": 30,
    "Pedro": 28,
    "Ana": 22,
    "Carlos": 35,
    "Beatriz": 20,
    "Luiz": 32,
    "Gabriela": 29,
    "Rafael": 27,
    "Lucia": 26
}

# Gera uma lista aleatória de nomes e idades
lista_aleatoria = list(nomes.items())

# Ordena a lista em ordem alfabética por nome
lista_ordenada = sorted(lista_aleatoria, key=lambda x: x[0])

# Imprime a lista ordenada
for nome, idade in lista_ordenada:
    print(f"Nome: {nome}, Idade: {idade} anos")