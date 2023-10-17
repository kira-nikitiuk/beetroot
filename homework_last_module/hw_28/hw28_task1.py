import random
import time

def generate_random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]

def measure_sorting_time(arr, sorting_algorithm):
    start_time = time.time()
    sorted_arr = sorting_algorithm(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

array1 = generate_random_array(1000)
array2 = generate_random_array(10000)

sorted_array1_bubble, time_bubble1 = measure_sorting_time(array1.copy(), bubble_sort)
sorted_array1_selection, time_selection1 = measure_sorting_time(array1.copy(), selection_sort)
sorted_array1_merge, time_merge1 = measure_sorting_time(array1.copy(), merge_sort)

sorted_array2_bubble, time_bubble2 = measure_sorting_time(array2.copy(), bubble_sort)
sorted_array2_selection, time_selection2 = measure_sorting_time(array2.copy(), selection_sort)
sorted_array2_merge, time_merge2 = measure_sorting_time(array2.copy(), merge_sort)

with open('sorting_results.txt', 'w') as file:
    file.write("Результати сортування для масиву 1 (довжина 1000):\n")
    file.write(f"Bubble Sort: {time_bubble1:.6f} сек\n")
    file.write(f"Selection Sort: {time_selection1:.6f} сек\n")
    file.write(f"Merge Sort: {time_merge1:.6f} сек\n\n")

    file.write("Результати сортування для масиву 2 (довжина 10000):\n")
    file.write(f"Bubble Sort: {time_bubble2:.6f} сек\n")
    file.write(f"Selection Sort: {time_selection2:.6f} сек\n")
    file.write(f"Merge Sort: {time_merge2:.6f} сек\n")

print("Результати сортування збережено в файлі 'sorting_results.txt'.")
