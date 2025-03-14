class Elefante:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Elefante: {self.nome}"


class TamanhosElefantes:
    def __init__(self):
        self.elefantes = []

    def adicionar_elefante(self, nome):
        """Adiciona um elefante à lista."""
        novo_elefante = Elefante(nome)
        self.elefantes.append(novo_elefante)
        print(f"Elefante {nome} adicionado com sucesso!")

    def remover_elefante(self, nome):
        """Remove o elefante da lista pelo seu nome."""
        if nome in [elef.nome for elef in self.elefantes]:
            self.elefantes = [elef for elef in self.elefantes if elef.nome != nome]
            print(f"Elefante {nome} removido com sucesso!")
        else:
            print(f"Não foi possível encontrar o elefante {nome}.")

    def listar_elefantes(self):
        """Lista todos os elefantes da lista."""
        if self.elefantes:
            print("ELEFANTES CADASTRADOS:")
            for i, elef in enumerate(self.elefantes):
                print(f"{i+1}. {elef}")
        else:
            print("Nenhum elefante foi cadastrado.")


# Teste do script
if __name__ == "__main__":
    tamanhos_elefantes = TamanhosElefantes()
    
    while True:
        print("\n**OPÇÕES: **")
        print("1 - Adicionar elefante")
        print("2 - Remover elefante")
        print("3 - Listar elefantes")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome_elefante = input("Digite o nome do elefante a ser adicionado: ")
            tamanhos_elefantes.adicionar_elefante(nome_elefante)
        elif opcao == "2":
            nome_elefante = input("Digite o nome do elefante a ser removido: ")
            tamanhos_elefantes.remover_elefante(nome_elefante)
        elif opcao == "3":
            tamanhos_elefantes.listar_elefantes()
        elif opcao == "4":
            print("\nAté breve!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")