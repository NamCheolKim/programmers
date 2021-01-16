# 프로그래머스 Level 1 문자열 다루기 기본
s = "1234"


def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
    else:
        answer = False
    return answer
