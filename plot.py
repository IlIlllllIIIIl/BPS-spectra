from H_shape import Solver, save
r = [-3] + [-5] * 5
solver = Solver(r)
solver.find_all()

x = list(solver.get_det().keys())
# x = x[::-1]
y = list(solver.get_det().values())

import matplotlib.pyplot as plt
import numpy as np

plt.plot(x, y, linewidth=0.5)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("det_vs_ss_5.pdf") 
plt.close()

plt.scatter(x, y, s=0.5)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("scatter_5.png", dpi=300) 
plt.close()