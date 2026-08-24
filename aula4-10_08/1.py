import numpy as np
from scipy.stats import norm

#encontrando erro padrão da média amostral
dp = 10 / np.sqrt(25)

#encontrando a probabilidade
print(norm.cdf(95, 100, dp))