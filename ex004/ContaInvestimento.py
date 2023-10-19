"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. 
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""

class ContaInvestimento():
    def __init__(self, numeroConta, saldo, taxaJuros):
        self.numeroConta = numeroConta
        self.saldo = saldo  * taxaJuros + saldo 
        self.taxaJuros = taxaJuros
    
    def Depositar(self, valor):
        print(f"Saldo: R${self.saldo}")
        self.saldo += valor
        print(f"Saldo atual: R${self.saldo}")

    def Sacar(self, valor):
        print(f"Saldo: R${self.saldo}")
        self.saldo -= valor
        print(f"Saldo atual: R${self.saldo}")

    def ObterSaldo(self):
        self.saldo = self.saldo * self.taxaJuros
    
    def AdicionarJuros(self):
        self.saldo = (self.saldo * 0.05) + self.saldo
        print(f"Saldo com juros adicionado a 5%: R${self.saldo:.2f}")