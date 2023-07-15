"""
2) Crie uma classe que modele um retângulo:
a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e
Altura, a escolher)
b) Métodos:
i) Mudar valor dos lados
ii) Retornar valor dos lados
iii) Calcular Área
iv) Calcular Perímetro;
c) Crie um programa que utilize esta classe. Ele deve pedir
ao usuário que informe as medidas de um local. Depois,
deve-se criar um objeto com as medidas e calcular a
quantidade (em m2) de pisos (1 x 1 m2) e de rodapés
necessários para o local.
"""


class retangulo():
    def __init__(self,LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB

    def mudar_lados(self, ladoa, ladob):
        self.LadoA = ladoa
        self.LadoB = ladob

    def retorna_lados(self):
        return self.LadoA, self.LadoB

    def calcula_area(self):
        return self.LadoA * self.LadoB

    def calcula_perimetro(self):
        return (self.LadoA + self.LadoB) * 2


while True:
    largura = float(input("passe a largura do terreno: "))
    comprimento = float(input("passe o comprimento do terreno: "))

    casa = retangulo(largura,comprimento)

    print(f"vão ser necessários {casa.calcula_area()}m² de piso e {casa.calcula_perimetro()}m de rodapés")
