# Contexto: Cálculo de imposto. Questão: Peça ao usuário para inserir seu salário mensal.
# Calcule o imposto de renda com base no seguinte:
# até R$2000, isento; de R$2000,01 até R$3500, 10%; acima de R$3500, 15%.

from time import sleep

while True:
    try:
        salarioMensal = float(input("Digite o seu salário mensal: "))
        if salarioMensal <= 2000:
            print("Isento.")
        elif salarioMensal <= 3500:
            print(f"O imposto foi de {salarioMensal * 0.1}")
        else:
            print(f"O imposto foi de {salarioMensal * 0.15}")
        break
    except:
        print("Digite apenas números.")
        sleep(1.5)
