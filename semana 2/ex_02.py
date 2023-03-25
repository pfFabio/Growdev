'''
Escreva um programa que receba um número e escreva “Par”
caso esse número seja par e escreva “Impar” caso esse número seja impar.
 '''


def calcula(x):
    if x % 2 == 0:
        print("é par")
    else:
        print("é impar")


while True:
    num = float(input("me de um numero"))
    calcula(num)
