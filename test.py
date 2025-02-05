# from H_shape import Solver
import numpy as np
import itertools
from collections import defaultdict
import pandas as pd


class Solver:
    def __init__(self, ranges):
        self.ranges = ranges
        self.sol = defaultdict(list)  # Fix: Automatically handles missing indices
        self.det = 0  # Maximum determinant value found
    
    def solve(self):
        for a1 in self.ranges[0]:
            for a2 in self.ranges[1]:
                if a1 < a2 or a1 * a2 <= 1:
                    continue
                for a3 in self.ranges[2]:
                    val1 = -a2 - a3 + a1 * a2 * a3
                    if val1 >= 0: 
                        continue
                    for a4 in self.ranges[3]:
                        if a3 < a4:
                            continue
                        val2 = -a2 * a4 - a3 * a4 + a2 * a3 * (-1 + a1 * a4)
                        if val2 <= 0:
                            continue
                        for a5 in self.ranges[4]:
                            if a1 == a2 and a3 < a5:
                                continue
                            val3 = a4 - a2 * a4 * a5 + a3 * (1 - a2 * a5 - a4 * a5 + a1 * a4 * (-1 + a2 * a5))
                            if val3 >= 0:
                                continue
                            for a6 in self.ranges[5]:
                                if (a1 == a2 and a5 == a3 and a4 < a6) or (a5 < a6):
                                    continue
                                val4 = (a4 * (a5 + a6 - a2 * a5 * a6) + 
                                        a3 * (a6 - a1 * a4 * a6 + a5 * (1 - a2 * a6 - a4 * a6 + a1 * a4 * (-1 + a2 * a6))))                
                                
                                if val4 >= 1:  # Fix: Now dynamically supports all val4 values
                                    self.sol[val4].append((a1, a2, a3, a4, a5, a6))                               
                                    self.det = max(self.det, val4)  # Update max determinant

    def select(self, n):
        for a1 in self.ranges[0]:
            for a2 in self.ranges[1]:
                if a1 < a2 or a1 * a2 <= 1:
                    continue
                for a3 in self.ranges[2]:
                    val1 = -a2 - a3 + a1 * a2 * a3
                    if val1 >= 0: 
                        continue
                    for a4 in self.ranges[3]:
                        if a3 < a4:
                            continue
                        val2 = -a2 * a4 - a3 * a4 + a2 * a3 * (-1 + a1 * a4)
                        if val2 <= 0:
                            continue
                        for a5 in self.ranges[4]:
                            if a1 == a2 and a3 < a5:
                                continue
                            val3 = a4 - a2 * a4 * a5 + a3 * (1 - a2 * a5 - a4 * a5 + a1 * a4 * (-1 + a2 * a5))
                            if val3 >= 0:
                                continue
                            for a6 in self.ranges[5]:
                                if (a1 == a2 and a5 == a3 and a4 < a6) or (a5 < a6):
                                    continue
                                val4 = (a4 * (a5 + a6 - a2 * a5 * a6) + 
                                        a3 * (a6 - a1 * a4 * a6 + a5 * (1 - a2 * a6 - a4 * a6 + a1 * a4 * (-1 + a2 * a6))))                
                                
                                if val4 == n:
                                    self.sol[val4].append((a1, a2, a3, a4, a5, a6)) 


    # def select_n(self, n):
    #     # Create a 6D grid of all possible (a1, a2, ..., a6) values
    #     A1, A2, A3, A4, A5, A6 = np.meshgrid(*self.ranges, indexing='ij')

    #     # Compute intermediate values in bulk (vectorized calculations)
    #     val1 = -A2 - A3 + A1 * A2 * A3
    #     val2 = -A2 * A4 - A3 * A4 + A2 * A3 * (-1 + A1 * A4)
    #     val3 = A4 - A2 * A4 * A5 + A3 * (1 - A2 * A5 - A4 * A5 + A1 * A4 * (-1 + A2 * A5))
    #     val4 = (A4 * (A5 + A6 - A2 * A5 * A6) + 
    #             A3 * (A6 - A1 * A4 * A6 + A5 * (1 - A2 * A6 - A4 * A6 + A1 * A4 * (-1 + A2 * A6))))

    #     # Apply filtering conditions all at once (massive speedup)
    #     mask = (A1 >= A2) & (A1 * A2 > 1) & (A3 >= A4) & (A1 != A2 | A3 >= A5) & \
    #             ((A1 != A2) | (A5 != A3) | (A4 >= A6)) & (A5 >= A6) & \
    #             (val1 < 0) & (val2 > 0) & (val3 < 0) & (val4 == n)

    #     # Extract valid tuples where conditions are satisfied
    #     results = np.column_stack([A1[mask], A2[mask], A3[mask], A4[mask], A5[mask], A6[mask]])

    #     return results.tolist()  # Convert NumPy array to list for compatibility

    def get_solutions(self):
        return dict(self.sol)  # Convert defaultdict to normal dict before returning
    
    def get_max_det(self):
        return self.det
    
    def test(self, n):
        print(f"Testing determinant {n}...")
        for a1 in self.ranges[0]:
            for a2 in self.ranges[1]:
                if a1 < a2 or a1 * a2 <= 1:
                    continue
                for a3 in self.ranges[2]:
                    val1 = -a2 - a3 + a1 * a2 * a3
                    if val1 >= 0: 
                        continue
                    for a4 in self.ranges[3]:
                        if a3 < a4:
                            continue
                        val2 = -a2 * a4 - a3 * a4 + a2 * a3 * (-1 + a1 * a4)
                        if val2 <= 0:
                            continue
                        for a5 in self.ranges[4]:
                            if a1 == a2 and a3 < a5:
                                continue
                            val3 = a4 - a2 * a4 * a5 + a3 * (1 - a2 * a5 - a4 * a5 + a1 * a4 * (-1 + a2 * a5))
                            if val3 >= 0:
                                continue
                            for a6 in self.ranges[5]:
                                if (a1 == a2 and a5 == a3 and a4 < a6) or (a5 < a6):
                                    continue
                                val4 = (a4 * (a5 + a6 - a2 * a5 * a6) + 
                                        a3 * (a6 - a1 * a4 * a6 + a5 * (1 - a2 * a6 - a4 * a6 + a1 * a4 * (-1 + a2 * a6))))                
                                
                                if val4 == n:
                                    print((a1, a2, a3, a4, a5, a6))
                                    self.sol[val4].append((a1, a2, a3, a4, a5, a6)) 



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

def save(solutions, filename, num_columns = 6):
    column_names = [f"a{i+1}" for i in range(num_columns)]

    # Create a DataFrame
    df = pd.DataFrame(solutions, columns=column_names)

    df.to_csv(filename, index=False)

    print(f"Solutions exported to {filename}")
    
    return 


r = [-5] + [-500] * 5
ranges = rangeN(r)

solver = Solver(ranges)
solver.test(1)
solver.test(2)
solver.select(3)

solutions = solver.get_solutions()

for i in solutions.keys():
    print(f"saving det{i} solutions")
    path_names = f"data/new_det{i}_200.csv"
    save(solutions[i], path_names)


