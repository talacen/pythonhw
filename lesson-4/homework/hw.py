def get_middle_three_chars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")

############################ 1

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Descending:", sorted_dict_desc)
print("Ascending:", sorted_dict_asc)

############################ 2

sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict) 

############################ 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict) 

############################ 4

def generate_squares(n):
    return {x: x*x for x in range(1, n+1)}

print(generate_squares(5))  

############################ 5

squares_dict = {x: x*x for x in range(1, 16)}
print(squares_dict)

############################ 2.1

my_set = {1, 2, 3, 4, 5}
print(my_set)  

############################ 2.2

sample_set = {"apple", "banana", "cherry"}

for item in sample_set:
    print(item)

############################ 2.3

sample_set = {1, 2, 3}
sample_set.add(4)  
sample_set.update([5, 6, 7])  
print(sample_set)  

############################ 2.4

sample_set = {1, 2, 3, 4, 5}
sample_set.remove(3) 
sample_set.discard(4) 
print(sample_set)  

############################ 2.5

sample_set = {10, 20, 30, 40}
item_to_remove = 20

if item_to_remove in sample_set:
    sample_set.remove(item_to_remove)

print(sample_set)  # Output: {10, 30, 40}

