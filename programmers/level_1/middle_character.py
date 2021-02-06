# 프로그래머스 Level 1 가운데 글자 가져오기

strs = "abcde"  # qwer


def solution(s):
    answer = len(s)
    if answer % 2 != 0:
        return s[int(answer // 2)]
    else:
        return s[int(answer // 2 - 1): int(answer // 2 + 1)]
    return answer


result = solution(strs)
print(result)
