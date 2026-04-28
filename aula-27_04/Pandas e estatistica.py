from collections import Counter
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#criando a base de dados:
dados = [14]*16 + [15]*12 + [16]*9 + [17]*3

#frequencia absoluta (fi)
fi = pd.Series(Counter(dados)).sort_index()
print(fi)

#frequencia absoluta acumulada(fia)
fia = fi.cumsum()
print(fia)

#frequencia relativa (fr)
fr = fi / fi.sum() * 100
print(fr)

#frequencia relativa acumulada (fra)
fra = fr.cumsum()
print(fra)

#montando a tabela
tabela = pd.DataFrame({
    'Frequencia_absoluta' : fi,
    'Frequencia_absoluta_acumulada' : fia,
    'Frequencia_relativa' : fr,
    'Frequencia_relativa_acumulada' : fra
})

#linha total na ultima linha
tabela.loc['Total'] = [
    fi.sum(),
    '-',
    fr.sum(),
    '-'
]
print(tabela)