import math
def square(side):
    return math.ceil(side * side)
side = int(input("Введите длину стороны: "))
print(f"Площадь квадрата: {square(side)}")
