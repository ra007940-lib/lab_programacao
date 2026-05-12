vetor = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

dif = 0

for i in range(10):
    rep = False

    for j in range(i):
        if vetor[i] == vetor[j]:
            rep = True

    if rep == False:
        dif = dif + 1

print("Quantidade de valores diferentes:", dif)