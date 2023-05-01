def calcula(media):
    if media < 4:
        return "E"
    elif media < 6:
        return "D"
    elif media < 7.5:
        return "C"
    elif media < 9:
        return "B"
    else:
        return "A"


while True:
    x = float(input("me de a 1ª nota: "))
    y = float(input("me de a 2ª nota: "))
    nota = (x+y) / 2
    conceito = calcula(nota)

    print(f"tirando a média das notas: {x} e {y} temos {nota} que resulta em {conceito}\nRESULTADO:\n")
    if conceito == "A" or "B" or "C":
        print("aprovado")
    else:
        print("reprovado")
