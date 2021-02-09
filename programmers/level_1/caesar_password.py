# 프로그래머스 Level 1 시저 암호

s = "a B z"
n = 4


def solution(s, n):
    answer = ""
    s = list(s)

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

        answer += s[i]

    return answer


result = solution(s, n)
print(result)
