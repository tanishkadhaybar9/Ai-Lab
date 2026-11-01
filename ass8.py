board = [' '] * 9

def winner(p):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(all(board[i] == p for i in w) for w in wins)

def minimax(ai):
    if winner('O'):
        return 1
    if winner('X'):
        return -1
    if ' ' not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if ai else 'X'
            scores.append(minimax(not ai))
            board[i] = ' '

    return max(scores) if ai else min(scores)

def show():
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        if i < 6:
            print('-----')

while True:
    show()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos not in range(9) or board[pos] != ' ':
        print("Invalid move!")
        continue

    board[pos] = 'X'

    if winner('X'):
        show()
        print("You Win!")
        break

    if ' ' not in board:
        show()
        print("Draw!")
        break

    best, move = -999, -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best:
                best, move = score, i

    board[move] = 'O'

    if winner('O'):
        show()
        print("AI Wins!")
        break

    if ' ' not in board:
        show()
        print("Draw!")
        break