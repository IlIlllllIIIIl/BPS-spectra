from H_shape import Solver, save


r = [-10] + [-10] * 5
solver = Solver(r)
for i in range(1,10):
    solver.select(i)
    path_names = f"test_det_{i}.csv"
    save(solver.get_solutions()[i], path_names)