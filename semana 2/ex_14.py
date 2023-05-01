def calcula(valor):
    if valor < 280:
        return valor * 1.2, "20%"
    elif valor < 700:
        return valor * 1.15, "15%"
    elif valor < 1500:
        return valor * 1.10, "10%"
    else:
        return valor * 1.05, "05%"


while True:
    salario = float(input("escreva o salário atual:"))
    novo_salario, taxa = calcula(salario)
    print(f"a) o salário antes do ajuste era: R${salario:.2f}\nb) o aumento foi de {taxa}")
    print(f"c)o aumento foi de R${novo_salario - salario:.2f}\nd)o novo valor é R%{novo_salario:.2f}\n\n")

