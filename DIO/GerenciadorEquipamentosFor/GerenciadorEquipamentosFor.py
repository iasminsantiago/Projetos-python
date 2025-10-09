# Gerenciador de Equipamentos
# Este script solicita ao usuário que insira até três equipamentos
# e depois exibe a lista completa com prefixo "-".

# Cria uma lista vazia para armazenar os equipamentos
itens = []

# Loop que solicita até 3 equipamentos ao usuário
for i in range(3):
    # Solicita o nome do equipamento
    item = input("Digite o nome do equipamento: ")
    
    # Adiciona o item à lista 'itens'
    itens.append(item)

# Exibe a lista completa de equipamentos
print("\nLista de Equipamentos:")
for item in itens:
    # Percorre cada item da lista e exibe com o prefixo "-"
    print(f"- {item}")
