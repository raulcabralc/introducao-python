# Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
#
#
# Dica: você pode pesquisar pela biblioteca randint para criar os valores de forma aleatória.
# o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

from random import randint

numbers = []
for i in range(0, 20):
    numbers.append(randint(0, 100))

print(numbers)

for k, v in enumerate(numbers):
    if v == max(numbers):
        print(f"Maior número: {v} | Posição: {k}")
    if v == min(numbers):
        print(f"Menor número: {v} | Posição: {k}")
