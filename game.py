# Функция для вывода игрового поля
def print_board(board):
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("   |   |   ")

# Функция для проверки выигрышной комбинации
def check_win(board, symbol):
    return ((board[0] == board[1] == board[2] == symbol) or
            (board[3] == board[4] == board[5] == symbol) or
            (board[6] == board[7] == board[8] == symbol) or
            (board[0] == board[3] == board[6] == symbol) or
            (board[1] == board[4] == board[7] == symbol) or
            (board[2] == board[5] == board[8] == symbol) or
            (board[0] == board[4] == board[8] == symbol) or
            (board[2] == board[4] == board[6] == symbol))

# Основная функция игры
def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_board(board)
    while True:
        # Ход игрока 1
        player1_choice = int(input("Игрок 1, выберите номер клетки для хода: "))
        if board[player1_choice-1] == "X" or board[player1_choice-1] == "O":
            print("Клетка уже занята. Попробуйте снова.")
            continue
        board[player1_choice-1] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("Игрок 1 победил!")
            break
        if all([x == "X" or x == "O" for x in board]):
            print("Ничья!")
            break
        # Ход игрока 2
        player2_choice = int(input("Игрок 2, выберите номер клетки для хода: "))
        if board[player2_choice-1] == "X" or board[player2_choice-1] == "O":
            print("Клетка уже занята. Попробуйте снова.")
            continue
        board[player2_choice-1] = "O"
        print_board(board)
        if check_win(board, "O"):
            print("Игрок 2 победил!")
            break


tic_tac_toe()
