import random

vetor = []
cont6 = 0

for i in range(50):
    dado = random.randint(1, 6)
    vetor.append(dado)

for i in range(50):
    if vetor[i] == 6:
        cont6 = cont6 + 1

percentual = (cont6 * 100) / 50

print("Lançamentos:", vetor)
print("Quantidade de vezes que saiu 6:", cont6)
print("Percentual de face 6:", percentual, "%")