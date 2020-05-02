import numpy as np

import grid_logic as grid
import step_first as step


def generate_solution(input_data: np.ndarray) -> np.ndarray:
    # code for generating solution string
    return step.process(input_data)


def validate_row(data: np.ndarray):
    for i in range(9):
        print("Column " + str(i))
        print(get_column(data, i))
        print("Row " + str(i))
        print(get_row(data, i))

    for i in range(1, 10):
        grid.get_grid_content(data, i)

    for i in range(0, 9):
        for j in range(0, 9):
            print(grid.get_grid_number(i, j), end="")
        print()


def get_column(data: np.ndarray, index) -> np.ndarray:
    return data[:, index]


def get_row(data: np.ndarray, index) -> np.ndarray:
    return data[index, :]

# def get_remaining_digits(data: np.ndarray) -> :
#
#
#     print()
