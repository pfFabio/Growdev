#as 2 linhas a seguir importam funções dos outros algoritimos criados nesse projeto
from arquivo import carrega_dados
from processamento import localiza,filtrar, projetar, atualizacao,salvar_arquivo, prof_agrupar


#le o arquivo "alunos - alunos" e prepara os dados para processar
lista, cabecalho = carrega_dados("alunos - alunos.csv", ',', [str, int, str, float, float, int, float, bool])


"""filtrado = filtrar(lista,'escola', "==", 'Pedro I')

atualizacao(lista, 'escola', '==', 'Pedro I', 'P1')

salvar_arquivo('aluno2.csv',',',filtrado,cabecalho)"""

print(prof_agrupar(lista,'escola'))
