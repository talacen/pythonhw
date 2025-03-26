############################  1
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(is_leap(2000))  
print(is_leap(1900)) 
print(is_leap(2024))  

############################  2
def check_weird(n):
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


check_weird(3) 
check_weird(24)  

############################ 3
def find_evens_if_else(a, b):
    if a % 2 != 0:
        a += 1  
    if b % 2 != 0:
        b -= 1  
    return list(range(a, b + 1, 2))


print(find_evens_if_else(3, 10)) 


def find_evens_no_if_else(a, b):
    return list(range(a + (a % 2), b + 1, 2))


print(find_evens_no_if_else(3, 10)) 

