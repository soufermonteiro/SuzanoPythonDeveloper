# Listas armazenam quais quer itens inclusive outras listas e objetos
# colchetes é mais utolizado para declarar uma lista

frutas = ["laranja", "maca", "uva"]
casas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# zero based

print(frutas[0])
print(letras[-1])
print(numeros[-5])
print()

# matriz bidimensional

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print()

# Fatiamento é passar o valor inicial ou final e acessar um conjunto de elementos
palavra = ["p", "y", "t", "h", "o", "n"]
print(palavra[2:])
print(palavra[:2])
print(palavra[1:3])
print(palavra[0:3:2])
print(palavra[::])
print(palavra[::-1])
print()

# For
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
print()

for indice, carro in enumerate(carros):
    print(f"{indice+1}: {carro}")
print()

# Compressão de listas
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
print()

quadrado = [numero **2 for numero in numeros]
print(quadrado)
