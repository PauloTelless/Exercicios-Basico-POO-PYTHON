"""Classe Pessoa: Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 5 cm."""

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def Envelhercer(self, anos):
        print(f"{self.nome} tinha {self.idade} anos e {self.altura:.2f} metros de altura")
        self.idade += anos

        if self.idade < 21:
            self.altura += 0.05
            print(f"Agora {self.nome} tem {self.idade} anos e {self.altura:.2f} metros de altura")
        else:
            print(f"Agora {self.nome} tem {self.idade} anos e {self.altura:.2f} metros de altura")

    def Engordar(self, quilo):
        print(f"{self.nome} tinha {self.peso:.2f}kg")
        self.peso += quilo
        print(f"Engordou {quilo:.2f}kg")
        print(f"Agora {self.nome} tem {self.peso:.2f}kg")

    def Emagrecer(self, quilo):
        print(f"{self.nome} tinha {self.peso:.2f} kg")
        self.peso -= quilo
        print(f"Emagreceu {quilo:.2f}kg")
        print(f"Agora {self.nome} tem {self.peso:.2f}kg")

    def Crescer(self, centimetros):
        print(f"{self.nome} tinha {self.altura:.2f} metros")
        self.altura += (centimetros/100)
        print(f"Aumentou {centimetros} centímetros") 
        print(f"Agora {self.nome} tem {self.altura:.2f} metros de altura")