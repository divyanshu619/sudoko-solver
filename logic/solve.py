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
        get_grid(data, (i))

def get_column(data: np.ndarray, index) -> np.ndarray:
    return data[:, index]


def get_row(data: np.ndarray, index) -> np.ndarray:
    return data[index, :]

def get_grid(data:np.ndarray, grid):

    if not (1 <= grid <= 9):
        print("Grid number should be between 1 to 9.")
        return

    print("Grid #"+str(grid))
    gridCol = grid % 3
    if gridCol==0:
        gridCol=3

    if grid <= 3:
        gridRow = 1
    elif grid <=6:
        gridRow = 2
    else:
        gridRow = 3

    for x in range((gridRow-1)*3, (gridRow-1)*3+3):
        for y in range((gridCol-1)*3, (gridCol-1)*3+3):
            print(data[x, y], end = " ")
        print()