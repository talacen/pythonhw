####################### 1
fruits = ["Apple", "Banana", "Cherry", "Orange", "Grapes"]
print(fruits[2]) 

####################### 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

####################### 3
numbers = [10, 20, 30, 40, 50]
extracted = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(extracted)  

####################### 4
movies = ["Inception", "Avatar", "Titanic", "Interstellar", "The Dark Knight"]
movies_tuple = tuple(movies)
print(movies_tuple)

####################### 5
cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
print("Paris" in cities)  

####################### 6
numbers = [1, 2, 3]
duplicated_list = numbers * 2
print(duplicated_list)  

####################### 7
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)  

####################### 8
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num_tuple[3:8])  

####################### 9
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))  

###################### 10
animals = ("dog", "cat", "lion", "elephant", "tiger")
print(animals.index("lion"))  

###################### 11
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)  

###################### 12
sample_list = [10, 20, 30, 40]
sample_tuple = (100, 200, 300)
print(len(sample_list))  
print(len(sample_tuple)) 

###################### 13
num_tuple = (5, 10, 15, 20, 25)
num_list = list(num_tuple)
print(num_list)

###################### 14
num_tuple = (10, 5, 40, 20, 30)
print(max(num_tuple)) 
print(min(num_tuple))  

###################### 15
words_tuple = ("apple", "banana", "cherry")
reversed_tuple = words_tuple[::-1]
print(reversed_tuple)  
