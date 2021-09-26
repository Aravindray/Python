import math

def f(x):
    return x **2
result=f(3)
print(result)

def area(base, height):
    return base * height / 2
answer = area(3, 4)
print (answer)

answer1 = area(10, 7.45)
print (answer1)

def perimeter(side1, side2, side3):
    return side1 + side2 + side3
''' res = perimeter(3, 5, 4)
print(res) '''

def semiperimeter(side1, side2, side3):
    return perimeter(side1 + side2 + side3) / 2

def area_hero(side1, side2, side3):
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi- side1) * (semi- side2) * (semi- side3))
    return area
print (area_hero(3, 4, 5))