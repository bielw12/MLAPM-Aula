import matplotlib.pyplot as plt

dados = [12,12,23,23,34,12,43,45,23,54,65,34]

plt.boxplot(dados, patch_artist=True , boxprops=dict(facecolor='green'))
plt.title('Boxplot')
plt.xlabel('fonte de pesquisa')
plt.ylabel('dados')
plt.show()
