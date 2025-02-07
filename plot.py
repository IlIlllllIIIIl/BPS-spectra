from H_shape import Solver, save
r = [-100] * 6
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
plt.savefig("det_vs_ss_100.pdf") 
plt.close()

plt.scatter(x, y, s=0.5)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("scatter_100.png", dpi=300) 
plt.close()


from star import StarSolver, save
r = [-100] * 4
solver2 = StarSolver(r)
solver2.find_all()
x = list(solver2.get_det().keys())
# x = x[::-1]
y = list(solver2.get_det().values())

plt.plot(x, y, linewidth=0.5)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("star_plot_100.pdf") 
plt.close()

plt.scatter(x, y, s=1)
plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("star_scatter_100.pdf") 
plt.close()
