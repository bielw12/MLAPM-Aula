'''
for i in range(5):
    print("Numero ", i)
'''

'''
n = 0

while n < 10:
    print('numero', n)
    n += 0.000000000000000000000000000000000001
    '''

'''
def area_trian(b, h):
    return (b * h ) / 2

print(area_trian(67, 89))
'''

'''
#importando arquivos
#Localizar o diretorio (workspace)

import os
print(os.getcwd())

#importando o
import pandas

dados1 = pandas.read_csv("DadosAula(2).txt", sep=" ", header=0)
'''

#arquivo xlsx
import pandas as pd

dados3 = pd.read_excel("DadosAula(2).xlsx", engine="openpyxl")
print(dados3)