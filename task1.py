from typing import List, Tuple

def find_min_max(arr: List[int]) -> Tuple[int, int]:
    if not arr:
        raise ValueError("Масив не може бути порожнім")

    def find_min_max_recursive(low: int, high: int) -> Tuple[int, int]:
        # Базовий випадок: один елемент
        if low == high:
            return arr[low], arr[low]

        # Базовий випадок: два елементи
        if high == low + 1:
            return (min(arr[low], arr[high]), max(arr[low], arr[high]))

        # Рекурсивний поділ
        mid = (low + high) // 2
        left_min, left_max = find_min_max_recursive(low, mid)
        right_min, right_max = find_min_max_recursive(mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

    return find_min_max_recursive(0, len(arr) - 1)

# 🔎 Тестовий приклад
if __name__ == "__main__":
    sample = [7, 3, 9, 1, 12, -5, 0, 8]
    result = find_min_max(sample)
    print(f"Мінімум і максимум у масиві {sample} -> {result}")
