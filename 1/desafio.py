num = int(input('Digite um número: '))
numList = []

for x in range(0, 11):
    numList.append(f'{num} x {x} = {num * x}\n')

with open("tabuada.txt", "w") as file:
    file.write("".join(numList))