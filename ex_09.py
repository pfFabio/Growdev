"""
Implemente um programa onde o usuário deve adivinhar as letras de uma
palavra por meio de palpites. A palavra deve ser mostrada inicialmente com
as letras substituídas por underlines, conforme exemplo abaixo.
dados => _ _ _ _ _
O usuário deve então palpitar sobre as letras que ele julga estarem na frase.
A cada letra que errar, ele perde 1 ponto. A cada letra que ele acertar a
mesma deve ser exibida na tela, exemplo:
Palpite: d
Saída: d _ d _ _
Se completar a frase o usuário ganha o jogo, se sua p
"""
import random

contador, pontos= 0, 0
palavra = []
tela = ['_', '_', '_', '_', '_']



nome_arquivo = "palavras com 5 letras.txt"

arquivo = open(nome_arquivo, 'r')

conteudo = arquivo.readlines()

for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].replace('\n', '')

print(conteudo)
termo = conteudo[random.randint(1, len(conteudo))]

for i in termo:
    palavra += [i]

print(termo)

print('Bem vindo ao jogo da forca:')
while contador < 5:
    print(f'vc tem {pontos} pontos')
    acerto = 0
    printa = ''
    print('\na palavra é: ' + termo)
    tentativa = input('\ndigite uma letra: ')

    for i in range(len(palavra)):
        if tentativa == palavra[i]:
            tela[i] = tentativa
            contador += 1
            acerto = 1
    if acerto == 1:
        print("você acertou e ganhou 1 ponto")
        for i in tela:
            printa += i
        print(printa)
        pontos += 1
    else:
        print('você errou e perdeu 1 ponto')
        pontos -= 1
print('Parabéns você ganhou!')
