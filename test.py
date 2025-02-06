from H_shape import Solver, save

r = [-10] + [-300] * 5 
solver = Solver(r)
for i in range(1, 101):
    solver.select(i)
    path_names = f"data/test_det_{i}_300.csv"
    save(solver.get_solutions()[i], path_names)
