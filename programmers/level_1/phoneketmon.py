# 프로그래머스 Level 1 폰켓몬

nums = [3, 1, 2, 3]


def solution(nums):
    if len(nums) // 2 <= len(set(nums)):
        return len(nums) // 2
    else:
        return len(set(nums))


result = solution(nums)
print(result)
