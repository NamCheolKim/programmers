# 프로그래머스 Level 1 두 개 뽑아서 더하기
number = [2, 1, 3, 4, 1]


def solution(numbers):
    return sorted(list(set([numbers[i] + numbers[j]
                            for i in range(len(numbers))
                            for j in range(i + 1, len(numbers))])))


result = solution(number)
print(result)
