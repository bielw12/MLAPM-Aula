import pandas as pd

#Analise exploratoria de dados - Medidas de tend. central - MEDIA:
x = pd.Series([8,9,9,7,78,4,9,8,7,4,5,6,7,6,7,5,4,4,7])
print("MEDIA:", x.mean())

print()

#Analise exploratoria de dados - Medidas de tend. central - MEDIANA:
print("MEDIANA", x.median())

print()

#Analise exploratoria de dados - Medidas de tend. central - MODA:
print("MODA:", x.mode())