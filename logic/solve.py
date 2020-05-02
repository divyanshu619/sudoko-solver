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


def get_column(data: np.ndarray, index) -> np.ndarray:
    return data[:, index]


def get_row(data: np.ndarray, index) -> np.ndarray:
    return data[index, :]
