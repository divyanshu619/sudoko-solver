import numpy as np

import grid_logic as grid


def process(data: np.ndarray) -> np.ndarray:
    # print("Process started...")
    # print("Previous array -")
    # print(data)

    while True:
        is_data_updated = False
        for i in range(0, 9):
            for j in range(0, 9):
                if data[i, j] == 0:
                    missing_numbers = get_missing_numbers(data, i, j)
                    if len(missing_numbers) == 1:
                        data[i, j] = missing_numbers[0]
                        is_data_updated = True

        if not is_data_updated:
            # print("Processed array -")
            # print(data)
            break

    # print("Process finished")
    return data


def get_missing_numbers(data, row, col) -> np.ndarray:
    all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    row_data = data[row, :]
    col_data = data[:, col]
    grid_data = grid.get_grid_content_by_index(data, row, col)
    found_numbers = np.concatenate([row_data, col_data, grid_data])
    found_numbers = np.sort(np.unique((found_numbers[found_numbers != 0])))

    missing_numbers = np.setdiff1d(all_numbers, found_numbers)

    return missing_numbers
