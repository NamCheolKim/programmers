# 프로그래머스 Level 1 평균 구하기
s = [5, 5]


def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]

    return answer / len(arr)


result = solution(s)
print(result)