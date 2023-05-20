import matplotlib.pyplot as plt


rotulos = ['socio1', 'socio2', 'socio3']
porcentagem = [51, 12, 22]

cores = ['r', 'b', 'y']

explode = [0, 0.1, 0.3]

plt.pie(porcentagem, labels = rotulos, colors=cores, shadow = True, autopct='%1.1f%%', explode = explode)
plt.show()