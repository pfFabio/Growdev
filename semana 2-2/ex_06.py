"""
Em uma eleição presidencial existem dois candidatos. Os votos são
informados através de códigos. Os dados utilizados para a contagem dos
votos obedecem à seguinte codificação:
a) 1,2 = voto para os respectivos candidatos
b) 3 = voto nulo
c) 4 = voto em branco;
Elabore um programa que leia o código de votação de 5 candidatos. Calcule
e escreva:

a) total de votos para cada candidato
b) total de votos nulos
c) total de votos em branco
"""



while True:
    giantdush, turdsandwich, nulo, branco = 0, 0, 0, 0
    print("COMEÇAM AS ELEIÇÕES!\n")
    for i in range(5):
        voto = int(input("os votos obedecem à seguinte codificação:\na) 1 = giandush || 2 = turdsandwich\nb) 3 = voto "
                         "nulo\nc) 4 = voto em branco;\npor favor digite o numero correspondente:\n"))

        match voto:
            case 1:
                giantdush += 1
            case 2:
                turdsandwich += 1
            case 3:
                nulo += 1
            case _:
                branco += 1
    print(f"Giant Dush teve {giantdush} votos\nTurd Sandwich teve {turdsandwich} votos\n{nulo} votos foram nulos\n"
          f"{branco} votos foram em branco\n\n\n")

    if giantdush > turdsandwich:
        print("Giant Dush venceu!")
    elif turdsandwich > giantdush:
        print("Turd Sandwich venceu!")
    else:
        print("tivemos um empate!")
