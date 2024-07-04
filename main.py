def sum(a, b, c):
    return a + b + c


def pBoard(xbro, ybro):
    zero = 'X' if xbro[0] else ('O' if ybro[0] else 0)
    one = 'X' if xbro[1] else ('O' if ybro[1] else 1)
    two = 'X' if xbro[2] else ('O' if ybro[2] else 2)
    three = 'X' if xbro[3] else ('O' if ybro[3] else 3)
    four = 'X' if xbro[4] else ('O' if ybro[4] else 4)
    five = 'X' if xbro[5] else ('O' if ybro[5] else 5)
    six = 'X' if xbro[6] else ('O' if ybro[6] else 6)
    seven = 'X' if xbro[7] else ('O' if ybro[7] else 7)
    eight = 'X' if xbro[8] else ('O' if ybro[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


def cWin(xbro, ybro):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for win in win_conditions:
        if sum(xbro[win[0]], xbro[win[1]], xbro[win[2]]) == 3:
            print("X wins the match")
            return 1
        if sum(ybro[win[0]], ybro[win[1]], ybro[win[2]]) == 3:
            print("O wins the match")
            return 0
    return -1


if __name__ == "__main__":
    xbro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ybro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe")

    while True:
        pBoard(xbro, ybro)
        if turn == 1:
            print("X's turn")
            move = int(input("Enter your move (0-8): "))
            xbro[move] = 1
        else:
            print("O's turn")
            move = int(input("Enter your move (0-8): "))
            ybro[move] = 1
        ccWin = cWin(xbro, ybro)
        if ccWin != -1:
            print("Match Over")
            break
        turn = 1 - turn
