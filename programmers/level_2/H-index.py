# 프로그래머스 Level 2 H-index

citations = [3, 0, 6, 1, 5]


def solution(citations):
    citations = sorted(citations)
    answer = len(citations)

    for i in range(answer):
        if citations[i] >= answer - i:
            return answer - i
    return 0


result = solution(citations)
print(result)
