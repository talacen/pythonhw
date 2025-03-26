# name = input('your name: ')
# age = input('your age: ')
# age10 = int(age)+ 10
# greet = f"hello {name}!, you will turn {age10} in 10 years"
# print(greet)

# num = int(input('enter number: ').strip())

# if num % 2 == 0:
#     print ('это четное число')
# else: 
#     print ('это не четное число')

# num1 = int(input('Введите первое число: ').strip())
# num2 = int(input('Введите второе число: ').strip())
# num3 = int(input('Введите третье число: ').strip())

# max_num = max(num1, num2, num3)
# print(f'Наибольшее число: {max_num}')

# num = int(input('enter number:' ).strip())

# counter = 1

# while counter <= num:
#     print(counter)
#     counter += 1

# def sum_of_even(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += num
#     return total

# numbers = [1, 2, 3, 4, 5, 6]
# print(sum_of_even(numbers))

# def count_vowels(text):
#     count = 0
#     vowels = 'aeiouAEIOU'
#     for sym in text:
#         if sym in vowels:
#             count += 1
#     return count

# text = 'stfu lil nigga'
# print(count_vowels(text))

# def average(numbers):
#     total_sum = sum(numbers)
#     count = len(numbers)
#     return total_sum / count

# numbers = [1,2,3,4,5,6,2,3]
# print(average(numbers))

# def positive_numbers(numbers):
#     return [num for num in numbers if num > 0]

# def reverse_str(text):
#     return text[::-1]

# print(reverse_str("hello"))

# def ispalindrome(text):
#     return text == text[::-1]
    
# print(ispalindrome("madam"))  # True  
# print(ispalindrome("racecar"))  # True  
# print(ispalindrome("hello"))  # False  

# import numpy as np

ls = [[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]]
arr = np.array(ls)
print(arr)



