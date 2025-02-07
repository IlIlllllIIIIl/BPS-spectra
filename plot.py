# from H_shape import Solver, save
# r = [-100] * 6
# solver = Solver(r)
# solver.find_all()

# x = list(solver.get_det().keys())
# x = x[::-1]
# y = list(solver.get_det().values())

# import matplotlib.pyplot as plt
# import numpy as np

# plt.plot(x, y, linewidth=0.5)
# plt.xlabel('Sample size')
# plt.ylabel('Determinant')
# plt.title('Determinants vs Sample size')
# plt.savefig("det_vs_ss_100.pdf") 
# plt.close()

# plt.scatter(x, y, s=0.5)
# plt.xlabel('Sample size')
# plt.ylabel('Determinant')
# plt.title('Determinants vs Sample size')
# plt.savefig("scatter_100.png", dpi=300) 
# plt.close()


from star import StarSolver, save
import matplotlib.pyplot as plt
import numpy as np

r = [-200] * 4
solver = StarSolver(r)
solver.find_all()

x_values = []
y_values = []
# x_ext = list(solver.get_det().keys())
# y_min = [min(values) for values in solver.get_det().values()]
# y_max = [max(values) for values in solver.get_det().values()]

for key, values in solver.get_det().items():
    x_values.extend([key] * len(values))  # Repeat key for each y-value
    y_values.extend(values)  # Collect all y-values

plt.scatter(x_values, y_values, s=0.5)
# plt.plot(x_ext, y_max, linewidth=0.5, color='red', linestyle='-', label="Max values")
# plt.plot(x_ext, y_min, linewidth=0.5, color='green', linestyle='-', label="Min values")


plt.xlabel('Sample size')
plt.ylabel('Determinant')
plt.title('Determinants vs Sample size')
plt.savefig("star_scatter_200.pdf") 
plt.close()
