import numpy as np


def read_data(number_of_entries, filename) -> (np.ndarray, np.ndarray):
    quizzes = np.zeros((number_of_entries, 81), np.int32)
    solutions = np.zeros((number_of_entries, 81), np.int32)
    for i, line in enumerate(open(filename, 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))
    return quizzes, solutions
