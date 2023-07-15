"""
5) Faça um programa completo utilizando funções e classes que:
a) Possui uma classe chamada Ponto, com os atributos x e y.
b) Possui uma classe chamada Retângulo, com os atributos
largura e altura.
c) Possui uma função para imprimir os valores da classe Ponto.
d) Possui uma função para encontrar o centro de um retângulo.
e) Você deve criar alguns objetos da classe Retangulo.
f) Cada objeto deve ter um vértice de partida, por exemplo, o
vértice inferior esquerdo do retângulo, que deve ser um objeto
da classe Ponto.
g) A função para encontrar o centro do retângulo deve retornar o
valor para um objeto do tipo ponto que indique os valores de x
e y para o centro do objeto.
h) O valor do centro do objeto deve ser mostrado na tela
"""

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def imprimir(self):
        print(f" x tem o valor de {self.__x}")
        print(f" y tem o valor de {self.__y}")


class retangulo():
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura
        self.__vertice = Ponto(0,0)

    def centro(self):
        return Ponto(self.__largura/2 , self.__altura/2)


pot1 = Ponto(6,5)

ret1 = retangulo(1, 2)
ret2 = retangulo(2, 4)
ret3 = retangulo(3, 6)
ret4 = retangulo(4, 8)

centr1 = ret1.centro()
print(" o centro do retangulo tem as seguintes coordenadas:")
centr1.imprimir()