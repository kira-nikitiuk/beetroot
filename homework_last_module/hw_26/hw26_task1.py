import random
import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_random_list(length):
    return sorted([random.randint(1, 1000) for _ in range(length)])

def measure_time(search_func, arr, target):
    start_time = time.time()
    result = search_func(arr, target)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, result

sample_lengths = [1000, 5000, 10000]

for length in sample_lengths:
    random_list = generate_random_list(length)
    target = random.choice(random_list)

    linear_time, linear_result = measure_time(linear_search, random_list, target)
    binary_time, binary_result = measure_time(binary_search, random_list, target)

    print(f"Sample Length: {length}")
    print(f"Target: {target}")
    print(f"Linear Search Time: {linear_time} seconds, Result Index: {linear_result}")
    print(f"Binary Search Time: {binary_time} seconds, Result Index: {binary_result}")
    print("=" * 40)

