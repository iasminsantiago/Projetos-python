# Classe UsuarioTelefone e encapsulamento dos atributos
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada do usuário
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número de telefone: ")
plano = input("Digite o plano do usuário: ")

# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario
