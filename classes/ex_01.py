"""1) Crie uma classe que modele uma bola:
a) Atributos
i) Cor
ii) Circunferência
iii) Material
b) Métodos
i) troca_cor
ii) mostra_cor"""



class bola():
    def __init__(self, cor, circunferencia):
        self.cor = cor
        self.circunferencia = circunferencia

    def troca_cor(self, nova):
        self.cor = nova

    def mostra_cor(self):
        print(self.cor)



