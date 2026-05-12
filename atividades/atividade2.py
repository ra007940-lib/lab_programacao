vetor = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

x = int(input("Digite o valor X: "))

posicao = -1

for i in range(5):
    if vetor[i] == x and posicao == -1:
        posicao = i

print("Posição:", posicao)