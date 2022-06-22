from typing import List


def twoMaxValues(array: List[int]) -> int:
    length = len(array)

    if length <= 1:
        raise ValueError('Длина массива 1 или массив пустой')

    max_1 = max_2 = array[1]

    for i in range(length):
        if array[i] > max_1:
            max_2 = max_1
            max_1 = array[i]

        elif array[i] > max_2 or max_1 == max_2:
            max_2 = array[i]

    return max_1, max_2


a = [-3, 40, -2, -40, 0]
print(twoMaxValues(a))
