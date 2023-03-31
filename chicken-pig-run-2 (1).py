
from typing import Any, List, NewType

try:
    async def __ignore() -> bool | None: ...
except:
    print('Needs Python 3.10 or higher')
    exit(1)

BoardType = NewType('BoardType', List[List[Any]])
ChickenType = NewType('ChickenType', Any)
PigType = NewType('PigType', Any)


def is_valid_pos_chicken(board: BoardType, n: int, x: int, y: int, pig: PigType = 'P', chicken: ChickenType = 'C') -> bool:

    if (board[x][y] == chicken):
        return False

    def intersects_with_pig(board: BoardType, x: int, y: int, pig: PigType = 'P', chicken: ChickenType = 'C') -> bool:
        try:
            if (board[x][y] == pig):
                return True
        except:
            pass
        return False

    # line
    for i in range(n):
        if intersects_with_pig(board, x, i, pig):
            return False

    # column
    for i in range(n):
        if intersects_with_pig(board, i, y, pig):
            return False

    # diagonals
    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        if intersects_with_pig(board, i, j, pig):
            return False
        i -= 1
        j -= 1

    i, j = x + 1, y + 1
    while i < n and j < n:
        if intersects_with_pig(board, i, j, pig):
            return False
        i += 1
        j += 1

    i, j = x - 1, y + 1
    while i >= 0 and j < n:
        if intersects_with_pig(board, i, j, pig):
            return False
        i -= 1
        j += 1

    i, j = x + 1, y - 1
    while i < n and j >= 0:
        if intersects_with_pig(board, i, j, pig):
            return False
        i += 1
        j -= 1

    return True


def print_board(board: BoardType) -> None:
    print()
    for l in board:
        print(' ', *l)
    print()


def create_board(n: int) -> BoardType:
    return BoardType([['-' for _ in range(n)] for _ in range(n)])


def n_animals(board: BoardType, row: int, col: int, current_pigs: int, current_chickens: int, chicken: ChickenType = 'C', pig: PigType = 'P'):

    if (current_pigs == number_pigs):
        return put_chicken(board, 0, 0, current_chickens, chicken, pig)

    i, j = row, col
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != '-':
                continue
            board[i][j] = pig
            current_pigs += 1
            n_animals(board, i, j, current_pigs,
                      current_chickens, chicken, pig)
            board[i][j] = '-'
            current_pigs -= 1
        col = 0


def put_chicken(board: BoardType, row: int, col: int, current_chickens: int, chicken: ChickenType = 'C', pig: PigType = 'P'):

    if (current_chickens == number_chickens):
        add_solution(board)
        return

    i, j = row, col
    for i in range(len(board)):
        for j in range(len(board)):
            if (not is_valid_pos_chicken(board, len(board), i, j, pig, chicken)):
                continue
            board[i][j] = chicken
            current_chickens += 1
            put_chicken(board, i, j, current_chickens)
            board[i][j] = '-'
            current_chickens -= 1
        col = 0


def add_solution(board):
    if (board_hash := hash(''.join([p for l in board for p in l]))) not in solutions:
        solutions.add(board_hash)


def take_size_board():
    while True:
        try:
            n = int(input('Tamanho do tabuleiro: '))
            if n <= 0:
                print("Numero deve ser maior do que zero")
                continue
            return n
        except ValueError:
            print("Valor invalido")


def take_pigs():
    while True:
        try:
            number_pig = int(input('Numero de porcos: '))
            if number_pig < 0:
                print("Numero deve ser positivo")
                continue
            return number_pig
        except ValueError:
            print("Valor invalido")


def take_chickens():
    while True:
        try:
            number_chicken = int(input('Numero de galinhas: '))
            if number_chicken < 0:
                print("Numero deve ser positivo")
                continue
            return number_chicken
        except ValueError:
            print("Valor invalido")


n = take_size_board()
global number_chickens
number_chickens = take_chickens()
global number_pigs
number_pigs = take_pigs()
sum_animals = number_pigs + number_chickens
if (n * n < sum_animals):
    exit(1)

board = create_board(n)

chicken = 'C'
pig = 'P'
solutions = set()


n_animals(board, 0, 0, 0, 0, chicken, pig)

print("Total numero de solucoes = ", len(solutions))
