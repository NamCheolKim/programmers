# 프로그래머스 Level 1 같은 숫자는 싫어
arr = [1, 1, 3, 3, 0, 1, 1]


def solution(number):
    answer = []
    answer.append(number[0])

    for i in range(1, len(number)):
        if number[i] != number[i - 1]:
            answer.append(number[i])
    return answer


result = solution(arr)
print(result)
