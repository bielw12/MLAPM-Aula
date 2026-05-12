import matplotlib.pyplot as plt

dados = [12,12,23,23,34,12,43,45,23,54,65,34]

plt.hist(dados, bins=3, color='green')
plt.xlabel('Intervalo de dados')
plt.ylabel('frequencia')
plt.title('histograma de dados')
plt.show()
