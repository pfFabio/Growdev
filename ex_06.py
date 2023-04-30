"""
Faça uma função que recebe por parâmetro o tempo de duração da produção
de uma peça em uma fábrica expressa em segundos e exibe esse tempo em
horas, minutos e segundos.
"""
import datetime

while True:
    segundos = int(input("quantos segundos demorar para fazer a peça"))
    tempo = str(datetime.timedelta(seconds=segundos))
    print("o tempo médio de produção é " + tempo)
