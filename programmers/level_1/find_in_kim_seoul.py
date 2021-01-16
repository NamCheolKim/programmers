# 프로그래머스 Level 1 서울에서 김서방 찾기
s = ["jane", "clean", "kim"]


def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "kim":
            answer = "김서방은 " + str(i) + "에 있다"
    return answer


result = solution(s)
print(result)
