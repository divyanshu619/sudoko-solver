import datareader
import solve

data = datareader.read_data()

correct_solutions = 0
incorrect_solutions = 0
index = 0
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

print("Total sudokus to solve : " + str(datareader.number_of_entries))
print("Correct solution : " + str(correct_solutions))
print("Incorrect solution : " + str(incorrect_solutions))
