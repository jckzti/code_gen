import random

# Lista de palavras e frases que podem ser combinadas
palavras = ["O", "sol", "brilha", "no", "céu", "azul", "como", "um", "canto", "suave"]

# Função para gerar frases aleatórias
def gera_frase():
    # Escolher uma palavra inicial e final da frase de forma aleatória
    inicio = random.choice(palavras)
    fim = random.choice(palavras)
    
    # Escolher duas palavras intermediárias, também de forma aleatória
    palavra1 = random.choice(palavras)
    palavra2 = random.choice(palavras)
    
    # Combinar as palavras para formar a frase
    frase = f"{inicio} {palavra1} {fim}, como {palavra2}."
    
    return frase

# Geração de 5 frases aleatórias
for _ in range(5):
    print(gera_frase())