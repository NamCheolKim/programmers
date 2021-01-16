# 프로그래머스 Level 1 두 정수 사이의 합
a = 3
b = 5


def solution(m, n):
    return range(min(a, b), max(a, b) + 1)


result = solution(a, b)
print(result)
