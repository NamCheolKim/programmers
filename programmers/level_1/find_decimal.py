# 프로그래머스 Level 1 소수 찾기
s = 10


def solution(n):
    answer = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in answer:
            answer -= set(range(2 * i, n + 1, i))

    return len(answer)


result = solution(s)
print(result)
