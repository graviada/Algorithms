from typing import List, Any


def partition(array: List[int], begin: int, end: int) -> int:
    # Опорный индекс делаем равным начальному. Данный индекс отвечает за число, которое будет отсортировано в конец
    pivot = begin

    # Рассматриваем обрезанный кусок массива, в который НЕ включен опорный элемент array[begin]. К нему мы обращаемся,
    # Отсортированный кусок остается справа в конце.
    for i in range(begin + 1, end + 1):

        # Смотрим, является ли число в обрезанном массиве меньше
        # или равным опорному элементу
        if array[i] <= array[begin]:
            # Если да, то мы увеличиваем индекс опорного элемента
            pivot += 1

            # Меняем местами значения под текущим индексом и увеличинным опорным индексом, т. е. постепенно
            # отодвигаем большее число в конец
            array[i], array[pivot] = array[pivot], array[i]

    # Завершаем цикл, создаем новый опорный элемент: меняем array[pivot] и
    # array[begin] местами
    array[pivot], array[begin] = array[begin], array[pivot]

    # Вернули индекс нового опорного элемента
    return pivot


# Реализация рекурсивной части
def quickSort_short(array: List[int], begin=0, end=None) -> List[int]:
    # Начальная инициализация
    if end is None:
        end = len(array) - 1

    def _quicksort(array: List[int], begin: int, end: int) -> Any:
        # Если мы перебрали весь массив, т. е. начальный индекс больше или равен концу сортировки, то выходим
        if begin >= end:
            return None

        # Просматриваем весь массив
        pivot = partition(array, begin, end)

        # Вместо конца массива стоит опорный индекс, поскольку мы закинули самое большое число в конец - массив там
        # отсортирован
        _quicksort(array, begin, pivot - 1)

        # Во время прохода по массиву меньшие числа могут застрять в середине. Поэтому мы смещаем начало на единицу
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


array = [29, 19, 47, 11, 6]
quickSort_short(array)
print(array)

print(quickSort_short.__annotations__)

