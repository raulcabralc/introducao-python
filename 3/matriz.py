from random import randint

matriz = []

for l in range(0, 5):
    temp = []
    for c in range(0, 5):
        temp.append(randint(0, 100))
    matriz.append(temp)

maiores = []

for row in range(len(matriz)):
    print(f"\nLinha {row + 1}\n")
    maiores.append(max(matriz[row]))
    for col in matriz[row]:
        print(col)

print(f"O maior número foi {max(maiores)}")
