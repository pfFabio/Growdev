import sympy as sy
import pandas as pd
import matplotlib.pyplot as plt


semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

matriz = pd.DataFrame({'semana_1': [30, 32, 31.5, 31, 33, 34, 33],
                       'semana_2': [32, 30, 28, 29, 30.5, 31, 29],
                        'semana_3': [33, 34, 35, 35, 34.5, 34, 33]},
                        index= semana)
toda_matriz = matriz.stack()

matriz_freq = toda_matriz.value_counts()

print("TABELA FREQUÊNCIA")
print(matriz_freq)

linha = sy.Line(matriz['semana_1'], semana)


plt.figure(1)
plt.title('Linear - 1ª semana')
plt.plot(matriz['semana_1'])

plt.figure(2)
plt.title('Linear - 2ª semana')
plt.plot(matriz['semana_2'])

plt.figure(3)
plt.title('Linear - 3ª semana')
plt.plot(matriz['semana_3'])
plt.show()


media_total = toda_matriz.mean()
print(f'\n\n\na média de todos os dados é {media_total:.2f}')
media_semana_1 = matriz['semana_1'].mean()
print(f'a média da 1ª semana é {media_semana_1:.2f}')
media_semana_2 = matriz['semana_2'].mean()
print(f'a média da 2ª semana é {media_semana_2:.2f}')
media_semana_3 = matriz['semana_3'].mean()
print(f'a média da 3ª semana é {media_semana_3:.2f}')

plt.figure(0)
plt.title('Boxplot - Geral')
plt.boxplot(toda_matriz)

plt.figure(1)
plt.title('Boxplot - 1ª semana')
plt.boxplot(matriz['semana_1'])

plt.figure(2)
plt.title('Boxplot - 2ª semana')
plt.boxplot(matriz['semana_2'])

plt.figure(3)
plt.title('Boxplot - 3ª semana')
plt.boxplot(matriz['semana_3'])
plt.show()


