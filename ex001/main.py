""" Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

from ContaCorrente import ContaCorrente

conta1 = ContaCorrente(12882,"Paulo Souza Telles Filho", 1000)
conta1.Depositar(500)
conta1.Sacar(250)
conta1.AlterarNome("Graziela Matheus Santos")