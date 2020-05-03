from typing import List, Any

import numpy as np

import common_logic as logic
import step_first as step


def generate_solution(input_data: np.ndarray) -> np.ndarray:
    # code for generating solution string
    return step.process(input_data)


def verify_solution(solved_sudoku: np.ndarray) -> bool:
    result = True
    for i in range(9):
        row_details = logic.get_row(solved_sudoku, i)
        col_details = logic.get_column(solved_sudoku, i)
        sub_grid_details = logic.get_grid_content(solved_sudoku, i + 1)
        result = check_numbers_in_array(row_details, result)
        if not result:
            return result
        result = check_numbers_in_array(col_details, result)
        if not result:
            return result
        result = check_numbers_in_list(sub_grid_details, result)
        return result


def check_numbers_in_array(input_array: np.ndarray, result: bool) -> bool:
    all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    diff = np.setdiff1d(all_numbers, input_array.tolist())
    if len(diff) > 0:
        result = False
    return result


def check_numbers_in_list(input_array: List[Any], result: bool) -> bool:
    all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    diff = np.setdiff1d(all_numbers, input_array)
    if len(diff) > 0:
        result = False
    return result
