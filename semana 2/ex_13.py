def tipo_triangulo(a, b, c):
    if a == b == c:
        print("é um triangulo equilátero")
    elif a == b or b == c or c == a :
        print("é um triangulo isósceles")
    else:
        print("é um triangulo escaleno")


while True:
    A = float(input("me de um lado do triangulo: "))
    B = float(input("me de outro lado do triangulo: "))
    C = float(input("me de outro lado do triangulo: "))
    tipo_triangulo(A, B, C)