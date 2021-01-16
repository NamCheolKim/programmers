# 프로그래머스 Level 1 콜라츠 추측
s = 1


def solution(num):

    if num == 1:
        return 0

    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1


result = solution(s)
print(result)