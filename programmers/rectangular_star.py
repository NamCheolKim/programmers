# 프로그래머스 Level 1 직사각형 별찍기

a, b = map(int, input().strip().split(' '))

answer = ('*' * a + '\n') * b

print(answer)
