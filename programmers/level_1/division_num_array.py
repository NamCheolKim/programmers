# 프로그래머스 Level 1 나누어 떨어지는 숫자 배열
s = [2, 36, 1, 3]


def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]


result = solution(s, 1)
print(result)