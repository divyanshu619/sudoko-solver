import numpy as np

import step_first as step


def generate_solution(input_data: np.ndarray) -> np.ndarray:
    # code for generating solution string
    return step.process(input_data)
