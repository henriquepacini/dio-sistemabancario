class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente")
            return
        self.saldo -= valor

    def extrato(self):
        print(f"Conta: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}")


def grava_conta(conta, arquivo):
    with open(arquivo, "w") as f:
        f.write(f"{conta.numero};{conta.titular};{conta.saldo};{conta.limite}\n")


def le_conta(arquivo):
    with open(arquivo, "r") as f:
        linha = f.readline()
    if not linha:
        return None
    numero, titular, saldo, limite = linha.strip().split(";")
    return Conta(numero, titular, float(saldo), float(limite))


def main():
    conta = Conta("123-4", "João", 120.0, 1000.0)
    grava_conta(conta, "contas.txt")

    conta_arquivo = le_conta("contas.txt")
    conta_arquivo.extrato()

    conta_arquivo.deposita(50.0)
    conta_arquivo.extrato()

    conta_arquivo.saca(20.0)
    conta_arquivo.extrato()


if __name__ == "__main__":
    main()