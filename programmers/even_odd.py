# 프로그래머스 Level 1 짝수와 홀수
n = 3


def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = solution(n)
print(result)
