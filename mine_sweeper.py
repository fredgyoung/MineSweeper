
import random

width = 10
height = 10
num_mines = 10
board = []


def create_board():

    for i in range(height):
        row = []
        for j in range(width):
            row.append('')
        board.append(row)

    for x in range(num_mines):

        duplicate = True

        while duplicate:
            i = random.randint(0, width-1)
            j = random.randint(0, height-1)
            #print(i, j)
            if board[i][j] == '':
                duplicate = False
                board[i][j] = '*'


def count_mines():

    count = 0

    for row in board:
        for cell in row:
            if cell =='*':
                count += 1

    print(count)


def print_board():

    for row in board:
        print(row)


if __name__ == '__main__':

    create_board()
    print_board()
    #count_mines()



