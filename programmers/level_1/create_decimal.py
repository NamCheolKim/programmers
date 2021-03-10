# 프로그래머스 Level 1 소수 만들기

import itertools

nums = [1, 2, 3, 4]


def solution(nums):
    answer = itertools.combinations(nums, 3)
    cnt = 0

    for i in answer:
        num = sum(i)
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            cnt += 1

    return cnt


result = solution(nums)
print(result)
