"""
7) Implemente uma classe chamada Carro com as seguintes
propriedades:
a) Um veículo tem um certo consumo de combustível (medidos
em km / litro) e uma certa quantidade de combustível no
tanque.
b) O consumo é especificado no construtor e o nível de
combustível inicial é 0.
c) Forneça um método andar() que simula o ato de dirigir o
veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina.

d) Forneça um método obter_gasolina(), que retorna o nível
atual de combustível e forneça um método
adicionar_gasolina(), para abastecer o tanque.
"""


class Carros():
    def __init__(self, consumo):
        self.__consumo = consumo
        self._tanque = 0

    def andar(self, distancia):
        self._tanque -= distancia / self.__consumo


    def adicionar_gasolina(self,quantidade):
        self._tanque += quantidade

    def obter_gasolina(self):
        teclado = input(f"o tanque tem {self._tanque} litros de combustivel, digite:\n1 -- abastecer\n2 -- voltar")
        if teclado == '1':
            abastece = float(input("digite a quantidade em litros a ser abastecido"))
            self.adicionar_gasolina(abastece)
            self.obter_gasolina()
        elif teclado == '2':
            print("dirija em segurança")
