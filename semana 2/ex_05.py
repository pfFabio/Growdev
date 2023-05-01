'''
Uma empresa vende um produto a R$5,40 a unidade. Sabendo-se que existe um desconto acumulado
de 0,5% do valor total da compra a cada centena comprada deste produto. Escreva um programa
que receba a quantidade comprada desse produto e informe.
a) O valor total da compra (sem o desconto)
b) A quantidade de centenas compradas desse produto
c) O desconto em R$.
d) O valor total da compra (com desconto)
'''


def calcula(venda):
    total = venda * 5.4
    centenas = venda/100
    total_final = total * (0.95 ** int(centenas))
    print(f"total de venda desse produto sem descontos foi: R${total:.2f}")
    print(f"houveram {centenas:.0f} descontos")
    print(f"o desconto total foi R${total - total_final:.2f}")
    print(f"o valor total com descontos foi: R${total_final}")


while True:
    quantidade = int(input("me informe a quantidade vendida"))
    calcula(quantidade)
