from H_shape import Solver, save

r = [-10] + [-200] * 5
solver = Solver(r)
solver.find_all()
solution = solver.get_det()
import matplotlib.pyplot as plt
import numpy as np

x = list(solution.keys())
y = list(solution.values())

plt.plot(x, y)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("determinant_ss_200.pdf") 
plt.close()