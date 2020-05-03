from datetime import datetime, timedelta

import datareader
import solve


def run_tests_from_data_set():
    # number_of_entries = 1
    # filename = 'sudoku-fail-test.csv'

    # number_of_entries = 10
    # filename = 'sudoku-small.csv'

    number_of_entries = 5000
    filename = 'sudoku-5k.csv'

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
    run_tests_from_data_set()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
