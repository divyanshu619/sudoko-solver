import datareader
import solve

data = datareader.read_data()

y = solve.generate_solution(data[0][0])
print(y)

solve.validate_row(data[0][0])
# for x in data[0]:
#     y = solve.generate_solution(x)
#     print(y)
