#numeros aleatórios
import random

print(random.sample(range(1,6), 4))

print([random.randint(1, 100)for _ in range (4)])


#numeros decimais (pseudoaleatorios)
print([random.uniform(1, 10) for _ in range (4)])


#arredondando
print([round(random.uniform(1, 10), 2) for _ in range (4)])


#numeros pseudoaleatorios viciados
random.seed(23)
print(([random.randint(1, 100)for _ in range (4)]))


#sorteio com nomes pseudoaleatorios
nomes =["paulao", "gabriel", "rodolfo", "matheus"]
print(random.sample(nomes, 2))

#sorteio com nomes viciados
nomes2 =["paulao", "gabriel", "rodolfo", "matheus"]
vies = [1, 0.2, 1, 0.1]
print(random.sample(nomes, 2))