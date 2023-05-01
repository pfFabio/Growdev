from datetime import datetime, timedelta

while True:
    ano = int(input("digite o ano com 4 digitos"))
    mes = int(input("digite o mês com 2 digitos"))
    dia = int(input("digite os dias com 2 digitos"))
    amanha = datetime(day=dia, month=mes, year=ano) + timedelta(1)
    print(f"amanhã será {amanha}")
