import pandas as pd
import matplotlib.pyplot as plt
x = pd.Series([8,9,9,7,78,4,9,8,7,4,5,6,7,6,7,5,4,4,7])

#gráfico boxplot
plt.boxplot(x, patch_artist=True,
            boxprops=dict(facecolor="red"))
plt.title('Boxplot')
plt.xlabel('fonte de pesquisa')
plt.ylabel('dados')
plt.show()