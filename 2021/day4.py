with open('./inputs/day4.txt') as file:
    numbers, *boards = file.read().rstrip().split('\n\n')
    numbers = [int(i) for i in numbers.split(',')]


class Board():
    def __init__(self, board, weight, height) -> None:
        self.board = board
        self.weight = 5
        self.height = 5

print(boards[0])

boards = [[line.split() for line in board.split('\n')] for board in boards]
boards = [[[int(elt) for elt in line] for line in board] for board in boards]

print(boards[0])



# board = Board(first_board)

# for k in range(5):
#     for j in range(5):
#         first_board[k][j] =



