from typing import List


# Будем сохранять все изначально в пустой список
def shuffleInOrder(list_1: List[int], list_2: List[int], currList: List[int],
                   resList: List[int]) -> List:
    if not list_1 or not list_2:
        currListCopy = currList.copy()
        currListCopy.extend(list_1)
        currListCopy.extend(list_2)
        resList.append(currListCopy)
        return

    num_1 = list_1.pop(0)
    currList.append(num_1)
    shuffleInOrder(list_1, list_2, currList, resList)
    list_1.insert(0, num_1)
    currList.remove(num_1)

    num_2 = list_2.pop(0)
    currList.append(num_2)
    shuffleInOrder(list_1, list_2, currList, resList)
    list_2.insert(0, num_2)
    currList.remove(num_2)

    return resList


print(shuffleInOrder([1, 3], [2, 4], [], []))
