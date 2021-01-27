# 프로그래머스 level 2 타겟넘버

n = [1, 1, 1, 1, 1]
t = 3

answer = 0


def dfs(idx, numbers, target, value):
    global answer
    numbers_list = len(numbers)

    if idx == numbers_list and value == target:
        answer += 1
        return

    if idx == numbers_list:
        return

    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)

    return answer


print(solution(n, t))
