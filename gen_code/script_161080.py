# Script: Porcos Felizes

# Importando bibliotecas necessárias
import random

# Definindo uma classe "Porco"
class Porco:
    def __init__(self, nome):
        self.nome = nome
        self.fome = True  # Começamos com a fome do porco ativa

    def comer(self):
        if self.fome:
            print(f"{self.nome} está comendo!")
            self.fome = False  # Desativamos a fome após o porco comer
            return True
        else:
            print(f"{self.nome} não precisa comer.")
            return False

    def brincar(self):
        if not self.fome:  # Apenas podemos brincar se o porco estiver satisfeito
            porco_estado = random.choice(["feliz", "preocupado"])
            if porco_estado == "feliz":
                print(f"{self.nome} está brincando e fazendo um barulho feliz!")
            else:
                print(f"{self.nome} parece estar com uma expressão preocupada.")
        else:
            print(f"{self.nome} precisa comer antes de brincar.")

# Criando alguns porcos
porco1 = Porco("Piggy")
porco2 = Porco("Hammy")

# Simulando atividades dos porcos
print("\nAtividades:")
porco1.comer()
porco1.brincar()
porco2.comer()
porco2.brincar()

print("\nFim do Script.")