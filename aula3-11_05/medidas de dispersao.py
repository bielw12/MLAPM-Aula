import pandas as pd

#Medidas de dispersao - MINIMO:
x = pd.Series([8,9,9,7,78,4,9,8,7,4,5,6,7,6,7,5,4,4,7])
print("Minímo:", x.min())

print()

#Medidas de dispersao - MAXIMO:
print("Máximo", x.max())

print()

#Medidas de dispersao - AMPLITUDE (DIFERENÇA ENTRE MÍNIMO E MÁXIMO:
print("Amplitude:", x.max() - x.min())

print()

#Medidas de dispersao - VARIANCIA:
print("Variância:", x.var())

print()

#Medidas de dispersao - DESVIO PADRAO:
print("Desvio Padrão", x.std())

print()

#Medidas de dispersao - Coeficiente de Variação:
print("Coeficiente de variação:", x.std() / x.mean() * 100)