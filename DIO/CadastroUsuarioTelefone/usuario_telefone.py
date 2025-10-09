# Projeto: Cadastro de Usuário de Telefone
# Este script cria usuários de telefone com nome, número e plano.
# Demonstra conceitos de POO: classe, encapsulamento e métodos especiais.

# Criação da classe UsuarioTelefone
class UsuarioTelefone:
    # Método construtor da classe
    def __init__(self, nome, numero, plano):
        # Encapsulamento dos atributos (privados)
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Getter para acessar o nome (encapsulamento)
    @property
    def nome(self):
        return self.__nome

    # Método __str__ para representar o objeto como string
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada dos dados do usuário
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número de telefone: ")
plano = input("Digite o plano (Essencial, Prata ou Premium Fibra): ")

# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)

# Impressão da mensagem usando o método __str__
print(usuario)
