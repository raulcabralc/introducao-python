# Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e
# armazene os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a
# leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI,
# se o nome estiver entre os 5 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

clubes = [
    "África do Sul",
    "Mongólia",
    "Austrália",
    "Ajax",
    "Botafogo"
]

selecao = input("Digite a seleção desejada: ")
achou = False

for i in range(len(selecao)):

    if selecao.lower() == clubes[i].lower():
        print(f"ACHEI! {selecao}")
        achou = True

if achou == False:
    print("Achei não mago...")
