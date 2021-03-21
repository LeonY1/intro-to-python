import random

board = []
row_lengths = []
for index in range(7):
    board.append([])
    row_lengths.append(0)
    for _ in range(6):
        board[index].append(" ")


def check_four(points):
    for point_index in range(len(points) - 3):
        group_of_four = points[point_index: point_index + 4]
        connected_flag = True

        for point in group_of_four:
            if point != group_of_four[0] or point == " ":
                connected_flag = False

        if connected_flag:
            return True
    return False


def check_row(row, col):
    points = board[row][max(0, col - 3): col + 1]
    return check_four(points)


def check_col(row, col):
    points = []
    for new_row_index in range(max(0, row - 3), min(7, row + 3)):
        points.append(board[new_row_index][col])
    return check_four(points)


def check_diagonal_1(row, col):
    points = []
    for new_row_index in range(max(0, row - 3), min(7, row + 3)):
        offset = (new_row_index - row)
        new_column_index = col + offset
        if 0 <= new_column_index <= 5:
            points.append(board[new_row_index][new_column_index])
    return check_four(points)


def check_diagonal_2(row, col):
    points = []
    for new_row_index in range(max(0, row - 3), min(7, row + 3)):
        offset = (new_row_index - row)
        new_column_index = col - offset
        if 0 <= new_column_index <= 5:
            points.append(board[new_row_index][new_column_index])
    return check_four(points)


def check_win(row):
    col = row_lengths[row] - 1
    print(row, col)
    if check_diagonal_1(row, col) or check_diagonal_2(row, col) or check_row(row, col) or check_col(row, col):
        return True
    return False


def add_marker(player, row):
    if row_lengths[row] == 6:
        print("Invalid Row chosen")
        return False
    current_column = row_lengths[row]
    board[row][current_column] = str(player)
    row_lengths[row] += 1
    print(row_lengths)
    return True


def print_board():
    print("_______________")
    for i in range(5, -1, -1):
        line = "|"
        for j in range(len(board)):
            line += board[j][i] + "|"
        print(line)
    print("---------------")
    print()


def main():
    print_board()
    cnt = 1
    while True:
        loc = random.randint(0, 6)
        if cnt % 2 == 0:
            while not add_marker("y", loc):
                loc = random.randint(0, 6)
        else:
            while not add_marker("r", loc):
                loc = random.randint(0, 6)
        cnt += 1
        print_board()
        if check_win(loc):
            break
    print("Final move played: (", loc, ",", row_lengths[loc] - 1, ")")


if __name__ == '__main__':
    main()
