# 프로그래머스 Level 1 제곱근 판별

import math

n = 121


def solution(n):
    answer = math.sqrt(n)

    if n % answer == 0:
        return (answer + 1) ** 2

    return -1


result = solution(n)
print(result)