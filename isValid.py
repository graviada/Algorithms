def isValid(s: str) -> bool:
    left = ['(', '{', '[']
    right = [')', '}', ']']
    length = len(s)
    answer = False

    if length % 2 != 0 or length < 1 or s[0] in right:
        return answer

    for i in range(length // 2):
        if length != 2:
            if s[i] in left and s[i + 1] in right:
                answer = True
            elif s[i] in left and s[i + length // 2] in right:
                answer = True

    return answer


s = "[}"
print(isValid(s))