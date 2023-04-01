"""
Crie uma estrutura bidimensional utilizando listas com sublistas para
representar um tabuleiro (1 lista com 20 elementos e cada elemento é uma
lista de 20 elementos, tabuleiro 20x20). Cada posição irá armazenar 1 valor
numérico que significa:
0 - Água
1 - Navio

Para cada posição escolha esses valores aleatoriamente, respeitando a regra
de que não podem existir mais de 20 navios no tabuleiro. Após os valores
serem distribuídos, o programa deve pedir ao usuário uma posição do
tabuleiro e informar se ele acertou um navio ou água e repetir o procedimento
até que o usuário derrote todos os navios ou chegue ao limite de 35
tentativas.
"""
import random

def preenche():
    global controle
    if controle < 20:
        conteudo = random.randint(0, 1)
        if conteudo == 1:
            controle += 1
        return conteudo
    else:
        return 0



while True:
    campo = []
    controle, vencer, turnos = 0, 0, 0
    for i in range(20):
        campo += [[preenche()]]
        for j in range(19):
            campo[i] += [preenche()]

    print(campo)
    print(f"temos {controle} barcos")
    while vencer < 20 and turnos < 35:
        x = int(input("me passe a coordenada x do seu tiro"))
        y = int(input("me passe a coordenada y do seu tiro"))
        if campo[x][y] == 1:
            print("voce acertou!")
            campo[x][y] = 0
            vencer += 1
        else:
            print("voce errou")
        if turnos == 34:
            print("atenção esta é a ultima tentativa")
    print("o jogo acabou! obrigado por jogar!")
