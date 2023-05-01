'''
Conversão de graus Celsius para Fahrenheit – Crie um programa que converta graus
Celsius em Fahrenheit. A fórmula é a seguinte: �� =95�� + 32
O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e,
em seguida, exiba a temperatura convertida em Fahrenheit.
Após construir esse programa, modifique-o para que converta graus Fahrenheit em
graus Celsius.
'''

def converteC(c):
    return c*9/5 + 32


def converteF(c):
    return (c - 32)*5/9


while True:
    caso = int(input("digite 1 para converter de Celsius -> Fahrenheit\ndigite 2 para converter Fahrenheit -> Celsius\n\n"))
    match caso:
        case 1:
            graus = float(input("me de os graus Celsius\n"))
            print(f"os graus em Fahrenheiut fica: {converteC(graus)}")

        case 2:
            graus = float(input("me de os graus Fahrenheit\n"))
            print(f"os graus em Celsius fica: {converteF(graus)}")
