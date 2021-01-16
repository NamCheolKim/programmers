# 프로그래머스 Level 1 제일 작은 수 제거하기
s = [4, 3, 2, 1]


def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
    else:
        arr.clear()
        arr.append(-1)

    return arr


result = solution(s)
print(result)
