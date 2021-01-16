# 프로그래머스 Level 1 나누어 떨어지는 숫자 배열
s = [2, 36, 1, 3]


def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer


result = solution(s, 1)
print(result)