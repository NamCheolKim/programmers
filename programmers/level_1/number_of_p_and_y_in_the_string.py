# 프로그래머스 Level 1 문자열 내 p와 y의 개수

strs = "pPoooyY"


def solution(s):
    answer = True

    s = s.lower()

    p = s.count('p')
    y = s.count('y')

    if p != y:
        return False

    return answer


result = solution(strs)
print(result)
