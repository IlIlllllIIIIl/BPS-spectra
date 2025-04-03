from H_shape import Solver, save
import sqlite3
import pandas as pd
import numpy as np


r = [-2] + [-5] * 5
solver = Solver(r)
solver.find_all()
all = solver.get_solutions()

flatsol = []
for key, matrix in all.items():
    for row, mat in enumerate(matrix):
        flatsol.append({"det": key, "row": row, **{f"col{j}": val for j, val in enumerate(mat)}})

conn = sqlite3.connect("H_all.db")
df = pd.DataFrame(flatsol)
df.to_sql("table1", conn, if_exists="replace", index=False)

conn.close()

# test1.ipynb file has the code to read off the series from the database

# example of searching for determinant 1
# r = [-2] + [-5] * 5
# solver = Solver(r)
# solver.select(1)
# sol = solver.get_solutions()
# save(sol[1], "H_1.csv")


# for i in all.keys():
#     if i <= 500:
#         path_names = f"data/H_shape/findall/det_{i}.csv"
#         save(all[i], path_names)

# for i in range(1,10):
#     solver.select(i)
#     path_names = f"H_shape/findall{i}.csv"
#     save(solver.get_solutions()[i], path_names)