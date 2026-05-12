import pandas as pd

#Medidas Separatrizes - QUARTIL:
x = pd.Series([8,9,9,7,78,4,9,8,7,4,5,6,7,6,7,5,4,4,7])
print("QUARTIL:")
print(x.quantile([0.25, 0.50, 0.75]))

print()

#Medidas Separatrizes - DECIL:
