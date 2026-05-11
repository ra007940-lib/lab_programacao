#Leia o valor n1
n1=int(input("Valor 1°: "))
#Leia o valor n2
n2=int(input("Valor 2°: "))
#Leia o valor n3
n3=int(input("Valor 3°: "))

Soma = n1 + n2 + n3
print(Soma)

#Exercício b
P1=float(input("Digite um valor: "))
P2=float(input("Digite um valor: "))
T=float(input("Digite um valor: "))
Pa=float(input("Digite um valor: "))
Provas=(3*P1)+(3*P2)
Média=(Provas + 3*T+Pa)/10
print(Média)
print(Provas)
#Exercício c
at=float(input("digite altura (em metros): "))
#PROCESSAMENTO
homem= (72.2*at)-58
mulher= (62.1*at)-44.7
#SAÍDA
print(f"h: {homem:.2f} kg")
print(f"M: {mulher:.2f} kg")