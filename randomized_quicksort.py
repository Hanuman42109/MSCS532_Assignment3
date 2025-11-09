import random
import time
import csv
import sys

# Increase recursion depth safely for larger inputs
sys.setrecursionlimit(10000)


# ---------------------------
# Randomized Quicksort
# ---------------------------
def randomized_quicksort(arr):
    """Sort an array using Randomized Quicksort."""
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)


# ---------------------------
# Deterministic Quicksort (Middle Pivot)
# ---------------------------
def deterministic_quicksort(arr):
    """Sort an array using Deterministic Quicksort (middle element pivot)."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    pivot = arr[mid]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)


# ---------------------------
# Benchmarking Utility
# ---------------------------
def benchmark(sort_fn, arr):
    """Measure execution time for a sorting function."""
    start = time.time()
    sort_fn(arr.copy())
    end = time.time()
    return end - start


# ---------------------------
# Main Execution
# ---------------------------
if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    results = []

    for n in sizes:
        print(f"\n=== Array Size: {n} ===")
        data_random = [random.randint(0, 10000) for _ in range(n)]
        data_sorted = list(range(n))
        data_reverse = list(range(n, 0, -1))
        data_duplicates = [random.choice(range(100)) for _ in range(n)]

        test_cases = [
            ("Random", data_random),
            ("Sorted", data_sorted),
            ("Reverse", data_reverse),
            ("Duplicates", data_duplicates)
        ]

        for case_name, data in test_cases:
            t_random = benchmark(randomized_quicksort, data)
            t_deterministic = benchmark(deterministic_quicksort, data)

            print(f"{case_name:10s} | Randomized: {t_random:.5f}s | Deterministic: {t_deterministic:.5f}s")

            results.append({
                "Array Size": n,
                "Input Type": case_name,
                "Randomized Time (s)": t_random,
                "Deterministic Time (s)": t_deterministic
            })

    # ---------------------------
    # Save results to CSV
    # ---------------------------
    with open("results.csv", "w", newline="") as csvfile:
        fieldnames = ["Array Size", "Input Type", "Randomized Time (s)", "Deterministic Time (s)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\n✅ Benchmark completed. Results saved to 'results.csv'")
    