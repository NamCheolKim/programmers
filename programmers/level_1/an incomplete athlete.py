# 프로그래머스 Level 1 완주하지 못한 선수
from collections import Counter

p = ["leo", "kiki", "eden"]
c = ["kiki", "eden"]


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]


result = solution(p, c)
print(result)
