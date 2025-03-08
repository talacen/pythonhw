import math

def square_properties(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

def circle_length(diameter):
    return math.pi * diameter

def mean(a, b):
    return (a + b) / 2

def number_operations(a, b):
    sum_ab = a + b
    product_ab = a * b
    square_a = a ** 2
    square_b = b ** 2
    return sum_ab, product_ab, square_a, square_b

print(square_properties(5))  
print(circle_length(10))
print(mean(4, 8))  
print(number_operations(3, 5))  
