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




nome_arquivo = "palavras com 5 letras.txt"

arquivo = open(nome_arquivo, 'r')

conteudo = arquivo.readlines()

for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].replace('\n', '')

print(conteudo)

