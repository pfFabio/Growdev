import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [40, 55, 30, 80]

rotulos = ['jan', 'fev', 'mar', 'abr']

plt.bar(x, y, color = 'red')
plt.xticks(x, rotulos) #substitui os valores do eixo X
plt.xlabel('meses') #rotulo geral do eixo X
plt.ylabel('total de vendas') #rotulo geral do eixo Y
plt.title('vendas em 2023')
plt.show()
