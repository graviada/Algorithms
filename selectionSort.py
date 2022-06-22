from typing import List


def selectionSort(array: List[int]):
    length = len(array)

    while length > 1:
        max_ = array[0]

        for i in range(length):
            if array[i] >= max_:
                max_ = array[i]
                j = i

        array[length - 1], array[j] = array[j], array[length - 1]
        length -= 1


array = [19, 47, 11, 6]
selectionSort(array)
print(array)
