# 프로그래머스 Level 1 이상한 문자 만들기

s = "try hello world"


def solution(s):
    answer = ""
    cnt = 0

    for i in range(len(s)):
        if cnt % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()

        cnt += 1

        if s[i].isspace():
            cnt = 0

    return answer


result = solution(s)
print(result)

