# 프로그래머스 Level 1 문자열 내림차순으로 배치하기
s = "Zbcdefg"


def solution(s):
    answer = ""
    str_arr = []

    for i in range(len(s)):
        str_arr.append(s[i])

    str_arr = sorted(str_arr, reverse=True)
    answer = "".join(str_arr)

    return answer


result = solution(s)
print(result)
