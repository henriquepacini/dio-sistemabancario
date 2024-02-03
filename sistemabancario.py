class Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def grava_cliente(self, cliente):
        with open(self.nome_arquivo, "a") as arquivo:
            arquivo.write(f"{cliente.nome};{cliente.cpf};{cliente.endereco}\n")

    def le_cliente(self, indice):
        with open(self.nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        cliente = linhas[indice].strip().split(";")
        return Cliente(cliente[0], cliente[1], cliente[2])

    def grava_conta(self, conta):
        with open(self.nome_arquivo, "a") as arquivo:
            arquivo.write(f"{conta.numero};{conta.cliente.nome};{conta.saldo};{conta.limite}\n")

    def le_conta(self, indice):
        with open(self.nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        conta = linhas[indice].strip().split(";")
        cliente = Cliente(conta[1], conta[2], "")
        return ContaBancaria(int(conta[0]), cliente, float(conta[3]), float(conta[4]))

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, numero, cliente, saldo=0, limite=1000):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para saque")
            return False

    def extrato(self):
        print(f"Numero da conta: {self.numero}")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Saldo: {self.saldo}")
        print(f"Limite: {self.limite}")

def main():
    arquivo = Arquivo("dados.txt")
    cliente = Cliente("João da Silva", "123.456.789-10", "Rua das Flores, 123")
    arquivo.grava_cliente(cliente)
    conta = ContaBancaria(1234, cliente)
    arquivo.grava_conta(conta)
    conta_carregada = arquivo.le_conta(0)
    conta_carregada.extrato()

if __name__ == "__main__":
    main()