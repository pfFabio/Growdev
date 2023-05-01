import datetime

while True:
    ano = int(input("digite o ano com 4 digitos"))
    mes = int(input("digite o mês com 2 digitos"))
    dia = int(input("digite os dias com 2 digitos"))
    if datetime.datetime(year=ano, month=mes, day=dia):
        print("ano válido")
