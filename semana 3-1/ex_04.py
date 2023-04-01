"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.
"""

while True:
    vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    res = []
    for i  in range(10):
        res += [vetor1[i]]
        res += [vetor2[i]]
    print(res)
    input()
