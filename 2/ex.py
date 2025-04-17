# Crie um programa que peça ao usuário para inserir várias notas de um aluno e
# calcule a média. Utilize um loop para continuar pedindo notas até que o
# usuário digite um valor específico para encerrar a entrada (por exemplo, -1).

notas = []
somaNotas = 0

print("Digite PARAR para ver a média e encerrar o programa.")
while True:
    try:
        num = float(input("Digite uma nota: "))
    except:
        break
    if num == -1:
        break
    notas.append(num)
    somaNotas += num

media = somaNotas / len(notas)

print(f"Média: {media:.2f}")
print(f"Ver notas? (Y/N)")
yn = str(input()).upper()

if yn == "Y":
    for i in notas:
        print(i)
