class ContaCorrente():
    def __init__(self, numeroConta, nomeCorrentista, saldo = 0):
        self.numeroConta = numeroConta
        numeroContaLista = [self.numeroConta]
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo  

    def AlterarNome(self, novoNome):
        print(f"Nome anterior: {self.nomeCorrentista}")
        self.nomeCorrentista = novoNome
        print(f"Nome atual: {self.nomeCorrentista}")

    def Depositar(self, valor):
        print(f"Valor depositado: R${valor}")
        self.saldo += valor
        print(f"Valor atual: R${self.saldo}")

    def Sacar(self, valor):
        self.saldo -= valor 
        print(f"Valor sacado: R${valor}")
        print(f"Valor atual: R${self.saldo}")
        if self.saldo == 0:
            print("Não existe mais valor a ser sacado")      
    