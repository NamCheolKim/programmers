# 프로그래머스 Level 1 하샤드의 수

arr = 10


def solution(x):
    answer = True

    num = 0

    for i in str(x):
        num += int(i)

    if x % num == 0:
        return answer

    return False


result = solution(arr)
print(result)