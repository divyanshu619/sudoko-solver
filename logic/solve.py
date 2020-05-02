import numpy as np


def generate_solution(input_data: np.ndarray) -> np.ndarray:
    # code for generating solution string
    return input_data


def validate_row(data: np.ndarray):
    for i in range(9):
        print("Column " + str(i))
        print(get_column(data, i))
        print("Row " + str(i))
        print(get_row(data, i))

    for i in range(1, 10):
        get_grid_content(data, i)

    for i in range(0, 9):
        for j in range(0, 9):
            print(get_grid_number(i, j), end = "")
        print()
    

def get_column(data: np.ndarray, index) -> np.ndarray:
    return data[:, index]


def get_row(data: np.ndarray, index) -> np.ndarray:
    return data[index, :]


def get_grid_number(row, col):
    if row < 3:
        gridRow = 1
    elif row < 6:
        gridRow = 2
    else:
        gridRow = 3

    if col < 3:
        gridCol = 1
    elif col < 6:
        gridCol = 2
    else:
        gridCol = 3

    if gridRow == 1:
        return gridCol
    elif gridRow == 2:
        return 3+gridCol
    else:
        return 6+gridCol    


def get_grid_content(data: np.ndarray, grid) -> np.ndarray:
    if not (1 <= grid <= 9):
        raise RuntimeError('Grid number should be between 1 to 9')

    print("Grid #" + str(grid))
    grid_col = grid % 3
    if grid_col == 0:
        grid_col = 3

    if grid <= 3:
        grid_row = 1
    elif grid <= 6:
        grid_row = 2
    else:
        grid_row = 3

    grid_content = []

    for x in range((grid_row - 1) * 3, (grid_row - 1) * 3 + 3):
        for y in range((grid_col - 1) * 3, (grid_col - 1) * 3 + 3):
            grid_content.append(data[x, y])

# def get_remaining_digits(data: np.ndarray) -> :
#
#
#     print()