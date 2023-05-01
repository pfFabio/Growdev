"""
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

def fibona(num):
    if num <= 1:
        return 1
    return fibona(num - 1) + fibona(num - 2)


quantidade = int(input("me de quantos numerosa da sequencia de fibbonacci voce quer ver: "))
for i in range(quantidade):
    print(fibona(i))
