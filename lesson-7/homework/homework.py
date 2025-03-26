# def func1(*args):
#     for i in args:
#         print(i)

# func1(20, 40, 60)
# func1(80, 100)


# def calculation(a, b):
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction

# res = calculation(40, 10)
# print(res)


# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)

# show_employee("Ben", 12000)
# show_employee("Jessa")



# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)


# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)

# showStudent = display_student
# showStudent("Emma", 26)


# x = [4, 6, 8, 24, 12, 2]
# print(max(x))



####################### 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))  
print(is_prime(7))  

####################### 2

def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(24))  
print(digit_sum(502))

####################### 3

def power_of_2(N):
    power = 1
    while power <= N:
        print(power, end=" ")
        power *= 2

power_of_2(10)
