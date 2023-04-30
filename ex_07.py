"""
 Escreva uma função que conte o número de espaços em branco em uma
frase passada como parâmetro
"""

def conta_espaço(frase):
    cont = 0
    for i in frase:
        if i == " ":
            cont += 1
    return cont


while True:
    texto = input("digite seu texto:\n")
    print(f"seu texto tem {conta_espaço(texto)} espaços")
