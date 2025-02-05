from H_shape.py import Solver
import numpy as np
import itertools
import pandas as pd


def rangeN(r):
    return [
        np.arange(r[0], 0),
        np.arange(r[1], 0),
        np.arange(r[2], -1),
        np.arange(r[3], -1),
        np.arange(r[4], -1),
        np.arange(r[5], -1)
    ]

def rangeall(r):
    return [
        np.arange(r[0], -r[0]),
        np.arange(r[1], -r[1]),
        np.arange(r[2], -r[2]),
        np.arange(r[3], -r[3]),
        np.arange(r[4], -r[4]),
        np.arange(r[5], -r[5])
    ]

r = [-10] * 6
ranges = rangeN(r)

solver = Solver(ranges)
solver.test(1)
solver.test(2)

solutions = solver.get_solutions()

for i in solutions.keys():
    print(f"saving det{i} solutions")
    path_names = f"det{i}_200.csv"
    solver.save(solutions.get(i), path_names)


