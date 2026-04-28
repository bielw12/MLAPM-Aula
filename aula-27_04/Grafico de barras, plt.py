import matplotlib.pyplot as plt
from collections import Counter

dados = ['sim'] * 20 + ['nao'] * 45
respostas1 = Counter(dados)

labels = list(respostas1.keys())
values = list(respostas1.values())

colors = ['skyblue']

plt.barh(labels, values, color=colors)
plt.title('respostas safadas')
plt.legend(labels, loc="upper right")
plt.show()
