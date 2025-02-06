from H_shape import Solver, save

r = [-10] + [-500] * 5 
solver = Solver(r)
solver.select(2)
solver.select(3)
solver.select(4)
solution = solver.get_solutions()
for i in solution.keys():
    path_names = f"data/det_{i}_500.csv"
    save(solution[i], path_names)
