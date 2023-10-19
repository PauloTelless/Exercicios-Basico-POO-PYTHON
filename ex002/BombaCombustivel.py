"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( )  método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( )  método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( )  altera o valor do litro do combustível.
alterarCombustivel( )  altera o tipo do combustível.
alterarQuantidadeCombustivel( )  altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""

class BombaCombustivel():
    def __init__(self, tipoCombustivel, valorCombustivel, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel.capitalize()
        self.valorCombustivel = valorCombustivel
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def AbastecerPorValor(self, valor):
        litros = valor/self.valorCombustivel
        print(f"Quantidade de litros na bomba: {self.quantidadeCombustivel:.2f} litros")
        self.quantidadeCombustivel -= litros
        if self.quantidadeCombustivel == 0:
            self.quantidadeCombustivel = 0
            print("A bomba está sem cobustível. Favor, reabastecer.")

        print(f"Foram abastecidos {litros:.2f} litros")
        print(f"Quantidade atual de litros na bomba: {self.quantidadeCombustivel:.2f} litros")
        print(f"Total a pagar R${valor:.2f}")
    
    def AbastecerPorLitro(self, litros):
        print(f"Quantidade de litros na bomba: {self.quantidadeCombustivel:.2f} litros")
        self.quantidadeCombustivel -= litros
        if self.quantidadeCombustivel < 0:
            self.quantidadeCombustivel = 0
            print("A bomba está sem combustível. Favor, reabastecer.")
            print("Total a pagar R$ 0.00")
        else:
            print(f"Foram colocados {litros:.2f} litros")
            print(f"Quantidade atual de litros na bomba: {self.quantidadeCombustivel:.2f} litros")
            print(f"Total a pagar R${litros*self.valorCombustivel:.2f}")

    def AlterarValorCombustivel(self, novoValor):
        print(f"Valor do combustível R${self.valorCombustivel:.2f}")
        self.valorCombustivel = novoValor
        print(f"Valor atual R$ {self.valorCombustivel:.2f}")
    
    def AlterarTipoCombustivel(self, novoCombustivel):
        print(f"Combustível anterior: {self.tipoCombustivel.capitalize()}")
        self.tipoCombustivel = novoCombustivel
        print(f"Combustível atual: {self.tipoCombustivel.capitalize()}")
        
        
    def AlterarQuantidadeCombustivel(self, novaQuantidadeCombustivel):
        print(f"Quantidade de combustível anterior: {self.quantidadeCombustivel:.2f} litros")
        self.quantidadeCombustivel = novaQuantidadeCombustivel
        print(f"Quantidade de combustível atual: {self.quantidadeCombustivel:.2f} litros")