# 프로그래머스 Level 1 크레인 인형뽑기 게임

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def check_get_doll(index, board):
    for i in range(len(board[index - 1])):
        # 같은 인형이 존재하면, 인형이 존재하는 값을 0으로 변경하고 사라진 인형의 갯수를 리턴.
        if board[index - 1][i] != 0:
            doll = board[index - 1][i]
            board[index - 1][i] = 0
            return doll


def solution(board, moves):
    board = list(map(list, zip(*board)))
    stack = []
    answer = 0

    for i in moves:
        check_doll = check_get_doll(i, board)

        if check_doll is not None:
            if not stack:
                stack.append(check_doll)
            elif stack[-1] == check_doll:
                answer += 2
                stack.pop()
            else:
                stack.append(check_doll)

    return answer


result = solution(board, moves)
print(result)
