# Classe UsuarioTelefone e encapsulamento
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if self.plano.verificar_saldo() >= custo:
            self.plano.deduzir_saldo(custo)
            saldo_restante = self.plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


# Classe Plano
class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        return self.__saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False


# Classe UsuarioPrePago (herança)
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Entrada do usuário
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número do usuário: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

destinatario = input("Digite o número do destinatário: ")
duracao = int(input("Digite a duração da chamada (minutos): "))

# Realiza a chamada
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
