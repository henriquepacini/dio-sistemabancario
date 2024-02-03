class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor
        return self.saldo

    def saca(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            print("Saldo insuficiente")
            return None

    def extrato(self):
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Limite: {self.limite}")


def grava_conta(conta, arquivo):
    with open(arquivo, "a") as file:
        file.write(f"{conta.numero};{conta.titular[0]};{conta.titular[1]};{conta.saldo};{conta.limite}\n")


def le_conta(arquivo):
    with open(arquivo, "r") as file:
        linha = file.readline()
        if not linha:
            return None
        numero, nome, cpf, saldo, limite = linha.strip().split(";")
        return Conta(int(numero), (nome, cpf), float(saldo), float(limite))


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    return (nome, cpf)


def cadastrar_conta(cliente):
    numero = int(input("Digite o número da conta: "))
    saldo = float(input("Digite o saldo inicial: "))
    limite = float(input("Digite o limite da conta: "))
    return Conta(numero, cliente, saldo, limite)


def main():
    cliente = cadastrar_cliente()
    conta = cadastrar_conta(cliente)
    grava_conta(conta, "contas.txt")
    conta_carregada = le_conta("contas.txt")
    if conta_carregada:
        conta_carregada.extrato()
        conta_carregada.deposita(100)
        conta_carregada.extrato()
        conta_carregada.saca(50)
        conta_carregada.extrato()


if __name__ == "__main__":
    main()