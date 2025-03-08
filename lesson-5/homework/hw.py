# def append_middle(s1, s2):
#     print("Original Strings are", s1, s2)
#     mi = int(len(s1) / 2)
#     x = s1[:mi:]
#     x = x + s2
#     x = x + s1[mi:]
#     print("After appending new string in middle:", x)

# append_middle("Ault", "Kelly")




# def mix_string(s1, s2):
#     first_char = s1[0] + s2[0]
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
#     res = first_char + middle_char + last_char
#     print("Mix String is ", res)

# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)



# def find_digits_chars_symbols(sample_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
#     for char in sample_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         else:
#             symbol_count += 1

#     print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

# sample_str = "P@yn2at&#i5ve"
# print("total counts of chars, Digits, and symbols \n")
# find_digits_chars_symbols(sample_str)