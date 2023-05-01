'''
Faça um programa para ler a quantidade adquirida e o preço unitário de um produto.
a) Calcular e escrever o total
total = quantidade adquirida * preço unitário
b) Leia o desconto sobre a compra e calcule.
total a pagar = total - desconto
i) Sabendo-se que:
(1) Se quantidade <= 5 o desconto será de 2%.
(2) Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
(3) Se quantidade > 10 o desconto será de 5%

'''


def calcula(quantidade, preço):
    total = quantidade * preço
    if quantidade <= 5:
        desconto = total * 0.02
    elif quantidade <= 10:
        desconto = total * 0.03
    elif quantidade > 10:
        desconto = total * 0.05

    print(f"o total gasto foi: R${total:.2f}")
    print(f"o total com desconto ficou: R${total - desconto:.2f}")


while True:
    quantidade = int(input("qual a quantidade de produtos adiquirida?\n"))
    valor = float(input("qual o valor unitário do produto"))
    calcula(quantidade, valor)

