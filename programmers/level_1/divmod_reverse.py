# 프로그래머스 Level 1 3진법 뒤집기
n = 45


def solution(n):
    div_mod = ''

    while n:
        div_mod += str(n % 3)
        n = n // 3

    answer = int(div_mod, 3)

    return answer


result = solution(n)
print(result)


