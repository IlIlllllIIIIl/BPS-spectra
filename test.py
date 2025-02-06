from H_shape import Solver, save

# r = [-2] + [-20] * 5
# solver = Solver(r)
# solver.find_all()
# solution = solver.get_det()
# series = solver.get_solutions()
# import matplotlib.pyplot as plt
# import numpy as np

# x = list(solution.keys())
# x = x[::-1]
# y = list(solution.values())

# plt.plot(x, y)
# plt.xlabel('Sample size')
# plt.ylabel('Determinant')
# plt.title('Determinants vs Sample size')
# plt.savefig("det_vs_ss_200.pdf") 
# plt.close()

# plt.scatter(x, y, s=1)
# plt.xlabel('Sample size')
# plt.ylabel('Determinant')
# plt.title('Determinants vs Sample size')
# plt.savefig("scatter_200.pdf") 
# plt.close()

# print(x[100:])

# save(solution, "det_vs_ss_200.txt")

r = [-10] + [-10] * 5
solver = Solver(r)
for i in range(1,10):
    solver.select(i)
    path_names = f"test_det_{i}.csv"
    save(solver.get_solutions()[i], path_names)