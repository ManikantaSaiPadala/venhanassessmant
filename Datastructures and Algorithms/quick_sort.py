from typing import List

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    p = arr[len(arr) // 2]
    le = [x for x in arr if x < p]
    m = [x for x in arr if x == p]
    r = [x for x in arr if x > p]

    return quicksort(le) + m + quicksort(r)

arr = [5,4,11,3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))