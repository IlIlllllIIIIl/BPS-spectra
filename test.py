from H_shape import Solver, save

r = [-2] + [-100] * 5
solver = Solver(r)
solver.find_all()
solution = solver.get_det()
import matplotlib.pyplot as plt
import numpy as np

x = list(solution.keys())
x = x[::-1]
y = list(solution.values())

plt.plot(x, y)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("det_vs_ss_200.pdf") 
plt.close()

plt.scatter(x, y, s=1)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("scatter_200.pdf") 
plt.close()