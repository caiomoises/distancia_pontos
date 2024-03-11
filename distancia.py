import math

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("A distância entre os dois pontos é: ", distancia)