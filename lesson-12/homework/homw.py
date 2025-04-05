import threading
from math import isqrt
from collections import defaultdict

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def check_primes(start, end, primes):
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)

def prime_checker_threaded(start, end, num_threads):
    primes = []
    threads = []
    range_size = (end - start) // num_threads

    for i in range(num_threads):
        sub_start = start + i * range_size
        sub_end = start + (i + 1) * range_size if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(sub_start, sub_end, primes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Prime numbers:", sorted(primes))

def count_words(lines, word_count):
    local_count = defaultdict(int)
    for line in lines:
        words = line.split()
        for word in words:
            local_count[word.lower()] += 1
    with threading.Lock():
        for word, count in local_count.items():
            word_count[word] += count

def word_count_threaded(filename, num_threads):
    word_count = defaultdict(int)
    threads = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], word_count))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    print("Prime Number Checker")
    prime_checker_threaded(1, 100, 4)

    print("\nFile Processing")
    word_count_threaded("file.txt", 4)
