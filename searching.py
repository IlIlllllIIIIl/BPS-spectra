from H_shape import Solver, save


r = [-2] + [-5] * 5
solver = Solver(r)
solver.find_all()
all = solver.get_solutions()

for i in all.keys():
    if i <= 500:
        path_names = f"data/H_shape/findall/det_{i}.csv"
        save(all[i], path_names)

# for i in range(1,10):
#     solver.select(i)
#     path_names = f"H_shape/findall{i}.csv"
#     save(solver.get_solutions()[i], path_names)