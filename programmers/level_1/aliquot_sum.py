# 프로그래머스 Level 1 약수의 합
s = 5


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer


result = solution(s)
print(result)
