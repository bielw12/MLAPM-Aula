import matplotlib.pyplot as plt

dados = ['sim']*20 + ['nao']*45

labels = ['nao','sim']
sizes = [45,20]
percent_labels = ['69,23%' , "30,77%"]
colors = ['red' , 'blue']

plt.pie(sizes, labels=percent_labels, colors=colors)
plt.title('Respostas entrevistas')
plt.legend(labels, loc='upper right')
plt.show()

