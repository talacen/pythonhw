def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(k):
    if k == 0:
        return 0
    return k % 10 + digit_sum(k // 10)

def powers_of_two(n):
    p = 1
    while p <= n:
        print(p, end=" ")
        p *= 2

print(is_prime(4)) 
print(is_prime(7))
print(digit_sum(24))  
print(digit_sum(502))
powers_of_two(10) 
