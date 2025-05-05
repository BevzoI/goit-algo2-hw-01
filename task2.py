import random
from typing import List

def quick_select(arr: List[int], k: int) -> int:
    if not (1 <= k <= len(arr)):
        raise ValueError("k повинно бути в межах від 1 до довжини масиву")

    def partition(low: int, high: int) -> int:
        # Випадковий вибір pivot для уникнення найгірших випадків (O(n^2))
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]

        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quick_select_helper(low: int, high: int, k_smallest: int) -> int:
        if low == high:
            return arr[low]

        pivot_index = partition(low, high)

        if k_smallest == pivot_index:
            return arr[pivot_index]
        elif k_smallest < pivot_index:
            return quick_select_helper(low, pivot_index - 1, k_smallest)
        else:
            return quick_select_helper(pivot_index + 1, high, k_smallest)

    return quick_select_helper(0, len(arr) - 1, k - 1)

# 🔎 Тестовий приклад
if __name__ == "__main__":
    sample = [7, 10, 4, 3, 20, 15]
    k = 4
    result = quick_select(sample, k)
    print(f"{k}-й найменший елемент у масиві {sample} -> {result}")
