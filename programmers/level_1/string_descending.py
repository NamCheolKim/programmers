# 프로그래머스 Level 1 문자열 내림차순으로 배치하기
s = "Zbcdefg"


def solution(s):
    answer = []
    change = ""

    for i in range(len(s)):
        answer.append(s[i])

    answer = sorted(answer, reverse=True)

    change = "".join(answer)

    return change


result = solution(s)
print(result)
