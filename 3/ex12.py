# Contexto: Determinação do tipo de triângulo. Questão: Peça ao usuário para inserir
# três lados de um triângulo e determine se é um triângulo equilátero, isósceles ou escaleno.

from time import sleep

lados = []

while True:
    try:
        for i in range(0, 3):
            lados.append(float(input("Digite um lado do triângulo: ")))
        if lados[0] == lados[1] == lados[2]:
            print("Triângulo equilátero.")
        elif len(set(lados)) < 3:
            print("Triângulo isósceles.")
        else:
            print("Triângulo escaleno.")
        break
    except:
        print("Digite apenas números.")
        sleep(1.5)
