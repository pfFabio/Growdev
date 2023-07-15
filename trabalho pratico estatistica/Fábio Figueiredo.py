import sympy as sy
from sympy.calculus.util import continuous_domain


t = sy.Symbol("x")
f = 4/(2+3*2**t)
if continuous_domain(f, t, sy.S.Reals) == sy.Reals: #checando se o dominio da função inclui todos os reais
    print('a) o dominio da função inclui todos os reais')

if sy.is_decreasing(f): #checando se a função é decrescente
    print('c)a função é decrescente')
else:
    print('c)a função é crescente')


print('d) o conjunto imagem pode ser representado da seguinte forma:')
print(sy.imageset(sy.Lambda(t, f), sy.Reals)) # retorna a imagem da função

sy.plot(4/(2+3*2**t)) # printo a função no final pra poder ter as resposta no terminal e a função na tela ao mesmo tempo

