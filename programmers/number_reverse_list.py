# 프로그래머스 Level 1 자연수 뒤집어 배열로 만들기
s = 12345


def solution(n):
    answer = list(map(int, reversed(str(n))))

    return answer


result = solution(s)
print(result)