import datareader
import solve

data = datareader.read_data()

for x in data[0]:
    y = solve.generate_solution(x)
    print(y)
