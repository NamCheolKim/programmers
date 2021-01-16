# 프로그래머스 Level 1 정수 내림차순으로 배치하기
s = 118372


def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)

    return int(''.join(answer))


result = solution(s)
print(result)
