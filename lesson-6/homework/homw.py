# s1 = "Abc"
# s2 = "Xyz"

# s1_length = len(s1)
# s2_length = len(s2)

# length = s1_length if s1_length > s2_length else s2_length
# result = ""

# s2 = s2[::-1]

# for i in range(length):
#     if i < s1_length:
#         result = result + s1[i]
#     if i < s2_length:
#         result = result + s2[i]

# print(result)


# def string_balance_test(s1, s2):
#     flag = True
#     for char in s1:
#         if char in s2:
#             continue
#         else:
#             flag = False
#     return flag


# s1 = "Yn"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)

# s1 = "Ynf"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)

####################### 1

def insert_underscore(txt):
    result = []
    count = 0

    for i in range(len(txt)):
        result.append(txt[i])
        if txt[i] not in "aeiou_" and (count + 1) % 3 == 0 and i < len(txt) - 1:
            result.append("_")
        count += 1

    return "".join(result)

print(insert_underscore("hello")) 
print(insert_underscore("assalom")) 
print(insert_underscore("abcabcabcdeabcdefabcdefg"))  

####################### 2

n = int(input())
for i in range(n):
    print(i**2)

####################### 3.1

i = 1
while i <= 10:
    print(i)
    i += 1

####################### 3.2

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


####################### 3.3

num = int(input("Enter number: "))
print("Sum is:", sum(range(1, num + 1)))

####################### 3.4

num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)

####################### 3.5

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 50 <= num <= 150:
        print(num)

####################### 3.6

num = input("Enter a number: ")
print(len(num))

####################### 3.7

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

####################### 3.8

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

####################### 3.9

for i in range(-10, 0):
    print(i)

####################### 3.10

for i in range(5):
    print(i)
print("Done!")

####################### 3.11

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if is_prime(num):
        print(num)

####################### 3.12

n_terms = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b

####################### 3.13

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter number: "))
print(f"{num}! =", factorial(num))

#######################  4

def uncommon_elements(list1, list2):
    return [x for x in list1 + list2 if x not in list1 or x not in list2]


print(uncommon_elements([1, 1, 2], [2, 3, 4]))  
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  

