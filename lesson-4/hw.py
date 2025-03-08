def get_middle_three_chars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")