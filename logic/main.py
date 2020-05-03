from datetime import datetime, timedelta

import numpy as np

import datareader
import solve


def solve_from_input_string(input_string: str):
    quiz = np.zeros(81, np.int32)
    for i, num in enumerate(input_string):
        quiz[i] = num
    quiz = quiz.reshape((9, 9))
    start_time = datetime.utcnow()
    solved = solve.generate_solution(quiz)
    completion_time = datetime.utcnow()
    time_delta: timedelta = (completion_time - start_time)
    result = solve.verify_solution(solved)
    if result:
        print("Solution generated successfully")
        print("Average time to solve : " + str(time_delta.total_seconds() * 1000) + " ms")
        print(solved)
    else:
        print("Could not generate solution")


def run_tests_from_data_set():
    number_of_entries = 1
    filename = 'sudoku-fail-test.csv'

    # number_of_entries = 10
    # filename = 'sudoku-small.csv'

    # number_of_entries = 5000
    # filename = 'sudoku-5k.csv'

    data = datareader.read_data(number_of_entries, filename)

    correct_solutions = 0
    incorrect_solutions = 0
    index = 0
    start_time = datetime.utcnow()
    for x, y in zip(data[0], data[1]):
        index += 1
        if index % 100 == 0:
            print("Sudokus solved : " + str(index))
        solved = solve.generate_solution(x)
        result = (solved == y).all()
        # print(solved)
        # print(y)
        if result:
            correct_solutions += 1
        else:
            print("-------------------------------------")
            print("Input : ")
            print(x)
            print("Actual : ")
            print(solved)
            print("Expected : ")
            print(y)
            print("-------------------------------------")
            incorrect_solutions += 1
    completion_time = datetime.utcnow()
    time_delta: timedelta = (completion_time - start_time)
    avg_time = (time_delta.total_seconds() * 1000) / number_of_entries
    print("Average time to solve : " + str(avg_time) + " ms")
    print("Total sudokus to solve : " + str(number_of_entries))
    print("Correct solution : " + str(correct_solutions))
    print("Incorrect solution : " + str(incorrect_solutions))


# Defining main function
def main():
    # input_string = '068700900004000071030809050300080100040005007007304092602001005000020600059030028'

    # expert
    # input_string = '080000000003900000901003002000032004307000000000064800000000090500040600260800500'
    # hard
    # input_string = '100304809024000007000960500230000050507008000000000400009500000300800000050600030'
    # ocr_out
    input_string = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'

    solve_from_input_string(input_string)
    # run_tests_from_data_set()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
