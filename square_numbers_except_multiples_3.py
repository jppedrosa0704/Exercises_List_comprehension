# Square numbers, except multiples of 3
# Create a list with the squares of numbers 1 to 20, but exclude numbers that are multiples of 3.

#traditional
lista = []
for x in range(1,21):
    if x%3 != 0:
        lista.append(x**2)
print(lista)

#listcomprehension
lista_comprehension = [x**2 for x in range(1,21) if x % 3 != 0]
print(lista_comprehension)
