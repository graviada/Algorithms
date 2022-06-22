from typing import List


def bubbleSort(array: List[int]):
    length = len(array)

    while length > 1:
        for i in range(length-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        length -= 1

    # return array


array = [19, 47, 11, 6]
bubbleSort(array)
print(array)