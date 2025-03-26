# 1

# try:
#     num = int(input("Enter a number: "))
#     result = num / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# 2

# try:
#     num = int(input("Enter an integer: "))
#     print("Valid integer:", num)
# except ValueError:
#     print("Error: Invalid input. Please enter an integer.")

# 3

# try:
#     with open("nonexistent_file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Error: The file does not exist.")

# 4

# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     print("Sum:", num1 + num2)
# except ValueError:
#     print("Error: Please enter only numbers.")

# 5

# try:
#     with open("/root/protected_file.txt", "w") as file:
#         file.write("Testing permission error")
# except PermissionError:
#     print("Error: Permission denied.")

# 6

# my_list = [10, 20, 30]
# try:
#     print(my_list[5])
# except IndexError:
#     print("Error: Index out of range.")

# 7

# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except KeyboardInterrupt:
#     print("\nError: Input canceled by user.")

# 8

# try:
#     result = 10 / 0
# except ArithmeticError:
#     print("Error: Arithmetic operation failed.")

# 9

# try:
#     with open("file.txt", "r", encoding="utf-8") as file:
#         content = file.read()
# except UnicodeDecodeError:
#     print("Error: Unicode decoding issue.")

# 10

# try:
#     my_list = [1, 2, 3]
#     my_list.append(4)
#     my_list.upper()  # Invalid method for a list
# except AttributeError:
#     print("Error: Invalid attribute used.")

# 2.1

# with open("example.txt", "r") as file:
#     print(file.read())

# 2.2

# n = 3
# with open("example.txt", "r") as file:
#     for _ in range(n):
#         print(file.readline().strip())

# 2.3

# with open("example.txt", "a") as file:
#     file.write("\nNew appended text.")

# with open("example.txt", "r") as file:
#     print(file.read())

# 2.4

# n = 3
# with open("example.txt", "r") as file:
#     lines = file.readlines()[-n:]
#     print("".join(lines))

# 2.5

# with open("example.txt", "r") as file:
#     lines = file.readlines()
# print(lines)

# 2.6

# with open("example.txt", "r") as file:
#     content = file.read()
# print(content)

# 2.7

# import numpy as np

# with open("example.txt", "r") as file:
#     data = np.array(file.readlines())
# print(data)

# 2.8

# with open("example.txt", "r") as file:
#     words = file.read().split()
# longest_word = max(words, key=len)
# print(longest_word)

# 2.9

# with open("example.txt", "r") as file:
#     line_count = sum(1 for _ in file)
# print("Total lines:", line_count)

# 2.10

# from collections import Counter

# with open("example.txt", "r") as file:
#     words = file.read().split()
# word_count = Counter(words)
# print(word_count)

# 2.11

# import os
# print("File size:", os.path.getsize("example.txt"), "bytes")

# 2.12

# data = ["apple", "banana", "cherry"]
# with open("output.txt", "w") as file:
#     for item in data:
#         file.write(item + "\n")

# 2.13

# with open("example.txt", "r") as source, open("copy.txt", "w") as dest:
#     dest.write(source.read())

# 2.14

# with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
#     for line1, line2 in zip(file1, file2):
#         print(line1.strip(), line2.strip())

# 2.15

# import random

# with open("example.txt", "r") as file:
#     lines = file.readlines()
# print(random.choice(lines))


# 2.16

# file = open("example.txt", "r")
# print("File closed:", file.closed)
# file.close()
# print("File closed:", file.closed)

# 2.17

# with open("example.txt", "r") as file:
#     content = file.read().replace("\n", " ")
# print(content)

# 2.18

# with open("example.txt", "r") as file:
#     words = file.read().split()
# print("Word count:", len(words))

# 2.19

# with open("example.txt", "r") as file:
#     characters = list(file.read())
# print(characters)

# 2.20

# import string

# for letter in string.ascii_uppercase:
#     with open(f"{letter}.txt", "w") as file:
#         file.write(f"This is {letter}.txt")

# 2.21

# import string

# n = 5  # Number of letters per line
# with open("alphabet.txt", "w") as file:
#     for i in range(0, len(string.ascii_uppercase), n):
#         file.write(" ".join(string.ascii_uppercase[i:i+n]) + "\n")

# others ######

# import string

# text = """Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""

# text = text.translate(str.maketrans("", "", string.punctuation)).lower()

# words = text.split()

# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)