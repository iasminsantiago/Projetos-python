# Projeto: Usuário de Telefone com Verificação de Saldo
# Este script cria usuários de telefone e associa planos com saldo, 
# demonstrando conceitos de POO: classes, encapsulamento e interação entre objetos.

# Classe que representa o plano de telefone
class PlanoTelefone:
    def __init__(self, nome, saldo):
        # Encapsulamento dos atributos
        self.__nome = nome
        self.__saldo = saldo

    # Método para retornar o saldo
    def verificar_saldo(self):
        return self.__saldo

    # Método para gerar mensagem personalizada com base no saldo
    def mensagem_personalizada(self):
        saldo = self.__saldo
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


# Classe que representa o usuário de telefone
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano  # recebe um objeto da classe PlanoTelefone

    # Método para verificar saldo e gerar mensagem personalizada
    def verificar_saldo(self):
        saldo = self.plano.verificar_saldo()
        mensagem = self.plano.mensagem_personalizada()
        return saldo, mensagem


# Recebendo entradas do usuário
nome_usuario = input("Digite o nome do usuário: ")
nome_plano = input("Digite o nome do plano (Essencial, Prata, Premium): ")
saldo_inicial = float(input("Digite o saldo atual do plano: "))

# Criação de objetos
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Verificação do saldo e exibição da mensagem personalizada
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
