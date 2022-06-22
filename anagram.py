from collections import Counter


def areAnagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    hashMap_1 = {}
    hashMap_2 = {}

    for char in s1:
        if char in hashMap_1:
            hashMap_1[char] += 1
        else:
            hashMap_1[char] = 1

    for char in s2:
        if char in hashMap_2:
            hashMap_2[char] += 1
        else:
            hashMap_2[char] = 1

    for key in hashMap_1:
        if key not in hashMap_2 or hashMap_1[key] != hashMap_2[key]:
            return False

    return True


def anotherSolution(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


print(areAnagrams('nameless', 'salesmen'))


# def char_frequency(word):
#     frequency = {}
#     for char in word:
#         #if character  is in frequency then increment the value
#         if char in frequency:
#             frequency[char] += 1
#         #else add character and set it to 1
#         else:
#             frequency[char] = 1
#     return frequency
#
#
# a_word ='google'
# b_word ='ooggle'
# #check length of the words
# if (len(a_word) != len(b_word)):
#    print ("not anagram")
# else:
#     #here we check the frequecy to see if we get the same
#     if ( char_frequency(a_word) == char_frequency(b_word)):
#         print("found anagram")
#     else:
#         print("no anagram")