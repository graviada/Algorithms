from typing import List


def minInList_Sorted(array: List[int]) -> int:
    def mergeSort(nums: List[int]) -> List[int]:
        length = len(nums)

        # Если список не пустой и не единичный
        if length > 1:
            # Разделяем список на 2 части
            center = len(nums) // 2
            left = nums[:center]
            right = nums[center:]

            # Сортируем отдельно обе половины списка
            mergeSort(left)
            mergeSort(right)

            # Теперь нужно отслеживать три индекса - i, j и k:
            # i — индекс в списке left,
            # j — индекс в списке right,
            # k — индекс в исходном списке array, в который в конечном итоге нужно
            # вставить все числа по порядку.

            i = j = k = 0

            # Если число из списка left меньше, чем число из списка right, мы
            # вставляем его в nums на позицию k, после чего увеличиваем индекс i на
            # единицу. Если число из списка right меньше или равно числу из списка
            # left, тогда оно отправляется в nums, а мы увеличиваем на единицу индекс
            # j. Наконец, после добавления любого из чисел в список nums, мы
            # увеличиваем на единицу индекс k.

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            # Цикл для перебора остатков элементов в списке
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

        return nums

    return mergeSort(array)[0]


def minInList_NotSorted(array: List[int]) -> int:
    min_value = array[0]

    for i in range(len(array)):
        if min_value > array[i]:
            min_value = array[i]

    return min_value


arr = [7, 9, 6, 1, 3]
# print(mergeSort(arr)[0])
print(minInList_Sorted(arr))
print(minInList_NotSorted(arr))
