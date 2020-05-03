from typing import Dict, List, Tuple

import numpy as np

import common_logic as logic


def process(data: np.ndarray) -> np.ndarray:
    while True:
        missing_number_grid = np.empty((9, 9), dtype=np.ndarray)
        is_data_updated = False
        for i in range(0, 9):
            for j in range(0, 9):
                if data[i, j] == 0:
                    missing_numbers = get_missing_numbers(data, i, j)
                    missing_number_grid[i, j] = missing_numbers
                    # print("[" + str(i) + "," + str(j) + "] : " + str(missing_numbers))
                    if len(missing_numbers) == 1:
                        data[i, j] = missing_numbers[0]
                        is_data_updated = True
        should_continue_row = update_values_row_wise(data, missing_number_grid)
        should_continue_column = update_values_column_wise(data, missing_number_grid)
        should_continue_sub_grid = update_values_sub_grid(data, missing_number_grid)
        if not (should_continue_row or should_continue_column or should_continue_sub_grid or is_data_updated):
            break
    # print(missing_number_grid)
    return data


def get_missing_numbers(data, row, col) -> np.ndarray:
    all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    row_data = logic.get_row(data, row)
    col_data = logic.get_column(data, col)
    grid_data = logic.get_grid_content_by_index(data, row, col)
    found_numbers = np.concatenate([row_data, col_data, grid_data])
    found_numbers = np.sort(np.unique((found_numbers[found_numbers != 0])))

    missing_numbers = np.setdiff1d(all_numbers, found_numbers)

    return missing_numbers


def update_values_row_wise(data: np.ndarray, missing_number_grid: np.ndarray) -> bool:
    should_continue_processing = False
    for i in range(9):
        number_occurrences_index_list: Dict[int, List[Tuple[int, int]]] = {}
        row_data: np.ndarray = logic.get_row(missing_number_grid, i)
        for j in range(9):
            cell = row_data[j]
            if cell is not None:
                for num in cell:
                    if num in number_occurrences_index_list.keys():
                        number_occurrences_index_list[num].append((i, j))
                    else:
                        number_occurrences_index_list[num] = [(i, j)]
        # print("-------------------------------------")
        # print("ROW : " + str(i))
        # print(number_occurrences_index_list)
        for k, v in number_occurrences_index_list.items():
            if len(v) == 1:
                should_continue_processing = True
                i = v[0][0]
                j = v[0][1]
                data[i, j] = k
                # print("[ROW] Updated value at position : " + str(v[0]) + " to : " + str(k))
    return should_continue_processing


def update_values_column_wise(data: np.ndarray, missing_number_grid: np.ndarray) -> bool:
    should_continue_processing = False
    for i in range(9):
        number_occurrences_index_list: Dict[int, List[Tuple[int, int]]] = {}
        col_data: np.ndarray = logic.get_column(missing_number_grid, i)
        for j in range(9):
            cell = col_data[j]
            if cell is not None:
                for num in cell:
                    if num in number_occurrences_index_list.keys():
                        number_occurrences_index_list[num].append((j, i))
                    else:
                        number_occurrences_index_list[num] = [(j, i)]
        # print("-------------------------------------")
        # print("COLUMN : " + str(i))
        # print(number_occurrences_index_list)
        for k, v in number_occurrences_index_list.items():
            if len(v) == 1:
                should_continue_processing = True
                i = v[0][0]
                j = v[0][1]
                data[i, j] = k
                # print("[COLUMN] Updated value at position : " + str(v[0]) + " to : " + str(k))
    return should_continue_processing


def update_values_sub_grid(data: np.ndarray, missing_number_grid: np.ndarray) -> bool:
    should_continue_processing = False

    for a in range(3):
        for b in range(3):
            number_occurrences_index_list: Dict[int, List[Tuple[int, int]]] = {}
            for c in range(3):
                for d in range(3):
                    x = c + (3 * a)
                    y = d + (3 * b)
                    cell = missing_number_grid[x, y]
                    if cell is not None:
                        for num in cell:
                            if num in number_occurrences_index_list.keys():
                                number_occurrences_index_list[num].append((x, y))
                            else:
                                number_occurrences_index_list[num] = [(x, y)]
            for k, v in number_occurrences_index_list.items():
                if len(v) == 1:
                    should_continue_processing = True
                    i = v[0][0]
                    j = v[0][1]
                    data[i, j] = k
                    # print("[SUB_GRID] Updated value at position : " + str(v[0]) + " to : " + str(k))

    return should_continue_processing
