######### 1 # defining prime number checker function

import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

######### 2 # defining threaded prime checking function

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

######### 3 # main program for prime checker

def main_prime_checker():
    start_range = 1
    end_range = 100
    num_threads = 4
    threads = []
    results = []

    step = (end_range - start_range) // num_threads
    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i != num_threads - 1 else end_range
        thread_result = []
        results.append(thread_result)
        thread = threading.Thread(target=check_primes, args=(start, end, thread_result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    primes = [num for sublist in results for num in sublist]
    print("Prime numbers found:", primes)

######### 2.1 # defining word count function

from collections import Counter

def count_words(lines, result):
    words = " ".join(lines).split()
    result.append(Counter(words))

######### 2.2 # defining threaded file processing function

def process_file(filename, num_threads=4):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread_result = []
        results.append(thread_result)
        thread = threading.Thread(target=count_words, args=(lines[start:end], thread_result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    word_counts = Counter()
    for result in results:
        word_counts.update(result[0])

    print("Word occurrences:", word_counts)

######### 2.3 # main program for file processing

def main_file_processing():
    filename = "large_text.txt"
    process_file(filename)

########## running programs

if __name__ == "__main__":
    print("Running Prime Checker:")
    main_prime_checker()
    print("\nRunning File Processing:")
    main_file_processing()
