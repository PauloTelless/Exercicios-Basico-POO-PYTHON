"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, 
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""

class BichinhoVirtual():
    def __init__(self, nome, fome = 50, saude = 50, idade = 2):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
    def AlterarNome(self, novoNome):
        print(f"O tamagushi se chamava {self.nome}")
        self.nome = novoNome
        print(f"O tamagushi agora se chama {self.nome}")
    
    def DarComida(self, comida):
        self.fome += comida
        print(f"Você alimentou {self.nome}")
        print(f"+{comida} de comida")
    
    def TirarComida(self, comida):
        self.fome -= comida
        print(f"Você tirou a comida de {self.nome}")
        print(f"-{comida} de comida")

    def AumentarSaude(self, pontoSaude):
        self.saude += pontoSaude
        print(f"Você aumentou a saúde de {self.nome}")
        print(f"+{pontoSaude} de saúde")
    
    def TirarSaude(self, pontoSaude):
        self.saude -= pontoSaude
        print(f"Você diminuiu a saúde de {self.nome}")
        print(f"-{pontoSaude} de saúde")
    
    def Humor(self):
        humor = self.fome + self.saude

        if humor >= 70:
            print(f"{self.nome} está feliz :)")

        if humor >= 30 and humor < 70:
            print(f"{self.nome} está precisando de cuidados :|")
        
        if humor >= 5 and humor < 30:
            print(f"{self.nome} está morrendo... T_T")
        
    def ExibirTamagushi(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nFome: {self.fome}\nSaúde: {self.saude}")
