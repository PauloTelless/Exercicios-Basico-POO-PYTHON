"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class TV():
    def __init__(self, canal = 0, volume = 0):
        self.canal = canal
        self.volume = volume

    def MudarCanal(self, novoCanal):
        print(f"Canal: {self.canal}")
        self.canal = novoCanal
        print(f"Canal atual: {self.canal}")
    
    def AumentarVolume(self):
        self.volume += 1
        if self.volume > 100:
            self.volume = 100
            print(f"O volume está no 100")
        else:
            print(f"+1 - Volume atual: {self.volume}")
    
    def DiminuirVolume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
            print("O volume está em 0")
            print("MUDO")
        else:
            print(f"-1 - Volume atual: {self.volume}")