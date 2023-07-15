"""
3) Crie uma classe para implementar uma conta corrente. A classe
deve possuir os seguintes atributos:
a) número da conta
b) nome do correntista
c) saldo
Os métodos são os seguintes:
a) alterar_nome
b) deposito
c) saque
No construtor, o saldo é opcional, com valor padrão zero e os
demais atributos são obrigatórios.
"""

class conta():
    def __init__(self, conta, nome, saldo = 0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def altera_nome(self, nome):
        self.nome = nome

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self,saque):
        self.saldo -= saque
