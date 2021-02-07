# 프로그래머스 Level 1 문자열 다루기 기본
s = "1234"


def solution(s):
    return s.isdigit() and len(s) in (4, 6)


result = solution(s)
print(result)
