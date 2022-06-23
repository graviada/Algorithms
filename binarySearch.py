from typing import List


def binarySearch(array: List[int], element: int) -> int:
    low_index = 0
    high_index = len(array) - 1

    while low_index <= high_index:
        middle = (low_index + high_index) // 2
        guess = array[middle]

        if element < guess:
            high_index = middle - 1
        elif element > guess:
            low_index = middle + 1
        else:
            return middle

    return None


my_list = [1, 3, 5, 7, 8, 9]
print(binarySearch(my_list, 8))