import time
import random
import matplotlib.pyplot as plt

# --- Sorting Algorithms ---

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# --- Input Generators ---

def generate_random(n):
    return [random.randint(0, 10000) for _ in range(n)]

def generate_sorted(n):
    return list(range(n))

def generate_reversed(n):
    return list(range(n, 0, -1))

def generate_nearly_sorted(n, swaps=10):
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# --- Testing Setup ---

sizes = [10, 100, 500, 1000]
input_types = {
    "Random": generate_random,
    "Sorted": generate_sorted,
    "Reversed": generate_reversed,
    "Nearly Sorted": generate_nearly_sorted
}
algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort
}

# --- Timing ---

results = {alg: {itype: [] for itype in input_types} for alg in algorithms}

for itype, gen_func in input_types.items():
    for size in sizes:
        data = gen_func(size)
        for alg_name, alg_func in algorithms.items():
            arr_copy = data.copy()
            start = time.time()
            if alg_name == "Merge Sort":
                alg_func(arr_copy)
            else:
                alg_func(arr_copy)
            duration = time.time() - start
            results[alg_name][itype].append(duration)

# --- Plotting ---

plt.figure(figsize=(12, 8))
for alg_name in algorithms:
    for itype in input_types:
        plt.plot(sizes, results[alg_name][itype],
                 label=f"{alg_name} - {itype}")
plt.title("Sorting Algorithms Performance on Different Input Types")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# --- Print Results to Terminal ---
print("\n--- Performance Results (Time in seconds) ---\n")
for alg_name in algorithms:
    for itype in input_types:
        times = results[alg_name][itype]
        for size, t in zip(sizes, times):
            print(f"{alg_name} | {itype:14s} | Size: {size:4d} | Time: {t:.6f}")
