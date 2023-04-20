"""
Crie um programa que calcule a folha de pagamento de uma empresa,
conforme as instruções a seguir:
a) O usuário pode inserir continuamente os nomes dos empregados até
que escolha a opção de finalizar o informe de dados;
b) Após informar o nome de cada empregado, o usuário deverá informar
o valor do salário da hora trabalhada desse empregado e quantas
horas ele trabalhou;
c) O programa deve calcular o salário bruto de cada empregado, a
percentagem de imposto retido na fonte (com base na tabela abaixo),
o valor do imposto retido na fonte e o salário líquido (pagamento bruto
menos imposto retido na fonte);
d) Depois que o usuário inserir os dados do último empregado, o
programa deve exibir o salário bruto, salário líquido, percentual de
imposto e valor do imposto para cada funcionário;
e) Por último, o programa deve exibir a soma de todas as horas
trabalhadas, o total da folha de pagamento bruta, o total de imposto e
a folha de pagamento líquida total.
"""


while True:
    nomes = []
    dinheiro_hora = []
    horas = []
    imposto = []
    impostoR = []
    salario_liquido = []
    salarios_brutos = []
    i = input("pressione enter para começar")
    while i != 'pare':
        i = input("digite o nome do empregado ou digite 'pare' para parar: ")
        if i != 'pare':
            nomes += [i]
            dinheiro = float(input("digite o valor da hora trabalhada por esse funcionário: "))
            horasT = int(input("digite a quantidade de horas trabalhadas por esse funcionário: "))
            salario_bruto = dinheiro * horasT
            if salario_bruto < 3000:
                imposto += [0.1]
                salario_liquido += [salario_bruto - salario_bruto * 0.1]
            elif salario_bruto < 5500:
                imposto += [0.13]
                salario_liquido += [salario_bruto - salario_bruto * 0.13]
            elif salario_bruto < 8000:
                imposto += [0.16]
                salario_liquido += [salario_bruto - salario_bruto * 0.16]
            else:
                imposto += [0.2]
                salario_liquido += [salario_bruto - salario_bruto * 0.2]
            horas += [horasT]
            salarios_brutos += [salario_bruto]



    for i in range(len(nomes)):
        impostoR += [salarios_brutos[i] * imposto[i]]
        print(f"\n\no salario bruto do {nomes[i]} foi R${salarios_brutos[i]:.2f}"
              f" resultando em um imposto de {imposto[i] * 100}%"
              f" que se iguala a RS{impostoR[i]:.2f} retidos de forma que"
              f" seu salario liquido foi R${salario_liquido[i]:.2f}")

    print(f"os funcionário trabalharam um total de {sum(horas)} horas")
    print(f"e receberam um total de R${sum(salarios_brutos):.2f} em valores brutos")
    print(f"contribuiram com um total de R${sum(impostoR):.2f} em impostos")
    print(f"recebendo assim um total de R${sum(salario_liquido):.2f} em salários líquidos")
