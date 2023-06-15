"""
6) Faça um programa completo utilizando classes e métodos que:
a) Possua uma classe chamada BombaCombustivel, com no
mínimo esses atributos:
i) tipo_combustivel.
ii) valor_litro
iii) quantidade_combustivel
b) Possua no mínimo esses métodos:

i) abastecer_por_valor() – método onde é informado o
valor a ser abastecido e mostra a quantidade de litros
que foi colocada no veículo
ii) abastecer_por_litro() – método onde é informado a
quantidade em litros de combustível e mostra o valor a
ser pago pelo cliente.
iii) alterar_valor() – altera o valor do litro do
combustível.
iv) alterar_combustivel() – altera o tipo do combustível.
v) alterar_quantidade_combustivel() – altera a
quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário
atualizar a quantidade de combustível total na bomba.
"""

class BombaCombustivel():
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_combustivel = quantidade_combustivel

    def abastecer_por_litro(self, litro):
        valor = litro * self.__valor_litro
        self.__quantidade_combustivel -= litro
        print(f"o abastecimento custou R${valor:.2f}")
        return valor

    def abastecer_por_valor(self, valor):
        litro = valor/ self.__valor_litro
        self.__quantidade_combustivel -= litro
        print(f"{litro} litros foram abastecidos")
        return litro

    def alterar_valor(self, novo_valor):
        self.__valor_litro = novo_valor

    def alterar_combustivel(self,novo_tipo):
        self.__tipo_combustivel = novo_tipo

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.__quantidade_combustivel = nova_quantidade
        
