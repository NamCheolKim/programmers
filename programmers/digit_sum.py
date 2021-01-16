# 프로그래머스 Level 1 자릿수 더하기
s = 987


def solution(n):
    n = list(map(int, str(n)))
    answer = 0
    for num in range(len(n)):
        answer += n[num]

    return answer


result = solution(s)
print(result)
