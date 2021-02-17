# 프로그래머스 Level 2 가장 큰 수

numbers = [6, 10, 2]


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(numbers)))


result = solution(numbers)
print(result)