"""
4) Crie uma classe que modele um Tamagochi (Bichinho Eletrônico):
a) Atributos
i) Nome
ii) Fome
iii) Saúde
iv) Idade.

b) Métodos
i) alterar_nome,
ii) alterar_fome
iii) alterar_saude
iv) alterar_idade
v) retornar_nome
vi) retornar_nome
vii) retornar_saude
viii) retornar_idade
"""


class tamagoshi():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self,nome):
        self.nome = nome

    def alterar_fome(self,fome):
        self.nome = fome

    def alterar_saude(self,saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade
