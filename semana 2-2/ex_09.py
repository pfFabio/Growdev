"""
Escreva um programa que receba o nome de 10 pessoas e para cada
pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:
a) Rio de Janeiro
b) Bahia
c) Minas Gerais
Após, informar qual foi o destino mais visitado e qual o menos visitado.
"""

while True:
    pessoas = []
    rj, bh, mg = 0, 0, 0
    for i in range(10):
        pessoas += [[input("qual o seu nome? ")]]
        pessoas[i] += [input("para onde você viajou?")]

    for i in range(len(pessoas)):
        match pessoas[i][1]:
            case "rio de janeiro":
                rj += 1
            case "bahia":
                bh += 1
            case "minas gerais":
                mg += 1

    if rj > bh and rj > mg:
        print("rio de janeiro foi o local mais visitado")
    elif bh > mg:
        print("bahia foi o local mais visitado")
    else:
        print("minas gerais foi o local mais visitado")

    if rj < bh and rj < mg:
        print("rio de janeiro foi o local menos visitado")
    elif bh < mg:
        print("bahia foi o local menos visitado")
    else:
        print("minas gerais foi o local menos visitado")