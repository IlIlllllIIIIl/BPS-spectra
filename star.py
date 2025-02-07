import itertools
import pandas as pd
import numpy as np

from collections import defaultdict

class StarSolver:    
    def __init__(self, ranges):
        self.ranges = ranges
        self.sol = defaultdict(list) 
        self.dict = defaultdict(list)
        self.series_in_order = defaultdict(list)
    
    def find_all(self):
        print(f"Searching for all negative definite solutions...")
        num = 1
        for a1 in range(self.ranges[0],0):
            for a2 in range(self.ranges[1],0):
                val0 = a1 * a2 -1
                if a1 * a2 <= 1:
                    continue
                for a3 in range(max(a2,self.ranges[2]),-1):
                    val1 = a3 * val0 - a2
                    if val1 >= 0: 
                        continue
                    for a4 in range(max(self.ranges[3], a3),-1):
                        val2 = a4 * val1 - a2 * a3
                        if val2 == int(val2) and val2 > 0:
                            self.sol[val2].append((a1, a4, a3, a2))
                            self.series_in_order[num].append((a1, a4, a3, a2))
                            self.dict[num].append(val2)
                            num += 1
                                
    def get_series(self):
        return dict(self.series_in_order)
    
    def get_det(self):
        return dict(self.dict)



    def select(self, n):
        print(f"Searching for determinant {n}...")
        for a1 in range(self.ranges[0],0):
            for a2 in range(self.ranges[1],0):
                val0 = a1 * a2 -1
                if a1 * a2 <= 1:
                    continue
                for a3 in range(max(a2,self.ranges[2]),-1):
                    val1 = a3 * val0 - a2
                    if val1 >= 0: 
                        continue
                    # for a4 in range(max(self.ranges[3], a3),-1):
                    a4 = (n + a2 * a3) / val1
                    if a4 == int(a4) and a4 < -1 and a4 >= a3:
                        self.sol[n].append((a1, a4, a3, a2))
                        # self.series_in_order[num].append((a1, a4, a3, a2))
                        # self.dict[num].append(val2)
                        # num += 1


    def get_solutions(self):
        return dict(self.sol)  # Convert defaultdict to normal dict before returning



def save(solutions, filename, num_columns = 4):
    column_names = [f"a{i+1}" for i in range(num_columns)]

    # Create a DataFrame
    df = pd.DataFrame(solutions, columns=column_names)

    df.to_csv(filename, index=False)

    print(f"Solutions exported to {filename}")
    
    return 


print("StarSolver loaded")