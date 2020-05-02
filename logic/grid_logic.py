from typing import List

import numpy as np


def get_grid_content_by_index(data, row, col) -> np.array:
    grid_number = get_grid_number(row, col)
    return get_grid_content(data, grid_number)


def get_grid_number(row, col):
    if row < 3:
        grid_row = 1
    elif row < 6:
        grid_row = 2
    else:
        grid_row = 3

    if col < 3:
        grid_col = 1
    elif col < 6:
        grid_col = 2
    else:
        grid_col = 3

    if grid_row == 1:
        return grid_col
    elif grid_row == 2:
        return 3 + grid_col
    else:
        return 6 + grid_col


def get_grid_content(data: np.ndarray, grid) -> List[any]:
    if not (1 <= grid <= 9):
        raise RuntimeError('Grid number should be between 1 to 9')

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

    return grid_content
