lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
print()
lista.clear()
print(lista)
print()


lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)
print()

l2 = lista.copy()
print(lista)
print(id(l2), id(lista))
print()

l2[0] = 5
print(l2)
print()

cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))
print()

linguagens = ["python", "js", "c"]
print(linguagens)
linguagens.extend(["java", "csharp"])
print(linguagens)
print()

print(linguagens.index("java"))
print(linguagens.index("python"))
print()

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))
print(linguagens)
print()

print(linguagens.remove("js"))
print(linguagens)
print()

numbers = [4, 21, 56, 3]
print(numbers)
numbers.reverse()
print(numbers)
print()
