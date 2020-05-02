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
        get_grid(data, i)


def get_column(data: np.ndarray, index) -> np.ndarray:
    return data[:, index]


def get_row(data: np.ndarray, index) -> np.ndarray:
    return data[index, :]


def get_grid(data: np.ndarray, grid) -> np.ndarray:
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

    for x in range((grid_row - 1) * 3, (grid_row - 1) * 3 + 3):
        for y in range((grid_col - 1) * 3, (grid_col - 1) * 3 + 3):
            print(data[x, y], end=" ")
        print()

# def get_remaining_digits(data: np.ndarray) -> :
#
#
#     print()
