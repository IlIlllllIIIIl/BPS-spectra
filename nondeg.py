import itertools

def solveP(ranges):
    sol = []
    
    # Now not nessarily negative definite. This function solves for determinant = +1.
    for a1 in ranges[0]:
        for a2 in ranges[1]:
            if a1 < a2: #or a1 * a2 <= 1:
                continue
            for a3 in ranges[2]:
                #if -a2 - a3 + a1 * a2 * a3 >= 0: 
                #    continue
                for a4 in ranges[3]:
                    if a3 < a4: # or -a2 * a4 - a3 * a4 + a2 * a3 * (-1 + a1 * a4) <= 0: 
                        continue
                    for a5 in ranges[4]:
                        if a1 == a2 and a3 < a5:
                            continue
                        #if a4 - a2 * a4 * a5 + a3 * (1 - a2 * a5 - a4 * a5 + a1 * a4 * (-1 + a2 * a5)) >= 0: 
                        #    continue
                        for a6 in ranges[5]:
                            if a1 == a2 and a5 == a3 and a4 < a6:
                                continue
                            if a5 < a6:
                                continue
                            if a4 * (a5 + a6 - a2 * a5 * a6) + a3 * (a6 - a1 * a4 * a6 + a5 * (1 - a2 * a6 - a4 * a6 + a1 * a4 * (-1 + a2 * a6))) == 1:
                                sol.append((a1, a2, a3, a4, a5, a6))
    return sol

def solveN(ranges):
    sol = []
    
    # Now not nessarily negative definite. This function solves for determinant = +1.
    for a1 in ranges[0]:
        for a2 in ranges[1]:
            if a1 < a2: #or a1 * a2 <= 1:
                continue
            for a3 in ranges[2]:
                #if -a2 - a3 + a1 * a2 * a3 >= 0: 
                #    continue
                for a4 in ranges[3]:
                    if a3 < a4: # or -a2 * a4 - a3 * a4 + a2 * a3 * (-1 + a1 * a4) <= 0: 
                        continue
                    for a5 in ranges[4]:
                        if a1 == a2 and a3 < a5:
                            continue
                        #if a4 - a2 * a4 * a5 + a3 * (1 - a2 * a5 - a4 * a5 + a1 * a4 * (-1 + a2 * a5)) >= 0: 
                        #    continue
                        for a6 in ranges[5]:
                            if a1 == a2 and a5 == a3 and a4 < a6:
                                continue
                            if a5 < a6:
                                continue
                            if a4 * (a5 + a6 - a2 * a5 * a6) + a3 * (a6 - a1 * a4 * a6 + a5 * (1 - a2 * a6 - a4 * a6 + a1 * a4 * (-1 + a2 * a6))) == -1:
                                sol.append((a1, a2, a3, a4, a5, a6))
    return sol

import pandas as pd

def save(num_columns, solutions, filename):
    column_names = [f"a{i+1}" for i in range(num_columns)]

    # Create a DataFrame
    df = pd.DataFrame(solutions, columns=column_names)

    df.to_csv(filename, index=False)

    print(f"Solutions exported to {filename}")
    
    return 

import numpy as np

#def range(r):
#    return [
#        np.arange(r[0], 0),
#        np.arange(r[1], 0),
#        np.arange(r[2], -1),
#        np.arange(r[3], -1),
#        np.arange(r[4], -1),
#        np.arange(r[5], -1)
#    ]

def rangeall(r):
    return [
        np.arange(-r[0],r[0]),
        np.arange(-r[1],r[1]),
        np.arange(-r[2], r[2])[(np.arange(-r[2], r[2]) != -1) & (np.arange(-r[2], r[2]) != 1)],
        np.arange(-r[3], r[3])[(np.arange(-r[3], r[3]) != -1) & (np.arange(-r[3], r[3]) != 1)],
        np.arange(-r[4], r[4])[(np.arange(-r[4], r[4]) != -1) & (np.arange(-r[4], r[4]) != 1)],
        np.arange(-r[5], r[5])[(np.arange(-r[5], r[5]) != -1) & (np.arange(-r[5], r[5]) != 1)]
    ]

def s4P(ranges):
    sol = []
    
    # Gauge: a2 >= a3 >= a4
    for a1 in ranges[0]:
        for a2 in ranges[1]:
            #if a1 * a2 <= 1:  # Prune invalid combinations
            #    continue
            for a3 in ranges[2]:
                if a2 < a3: #or -a2 - a3 + a1 * a2 * a3 >= 0: 
                    continue
                for a4 in ranges[3]:
                    if  a3 >= a4 and -a2 * a3 - a2 * a4 - a3 * a4 + a1 * a2 * a3 * a4 == 1:
                        sol.append((a1, a2, a3, a4))
    return sol

def s4N(ranges):
    sol = []
    
    for a1 in ranges[0]:
        for a2 in ranges[1]:
            for a3 in ranges[2]:
                if a2 < a3: 
                    continue
                for a4 in ranges[3]:
                    if  a3 >= a4 and -a2 * a3 - a2 * a4 - a3 * a4 + a1 * a2 * a3 * a4 == -1:
                        sol.append((a1, a2, a3, a4))
    return sol

def rs4(r):
    return [
        np.arange(-r[0], r[0]),
        np.arange(-r[1], r[1])[(np.arange(-r[1], r[1]) != -1) & (np.arange(-r[1], r[1]) != 1)],
        np.arange(-r[2], r[2])[(np.arange(-r[2], r[2]) != -1) & (np.arange(-r[2], r[2]) != 1)],
        np.arange(-r[3], r[3])[(np.arange(-r[3], r[3]) != -1) & (np.arange(-r[3], r[3]) != 1)]
    ]

r5_20 = [5] + [20]*5
sP5_20 = s4P(rs4(r5_20))
sN5_20 = s4N(rs4(r5_20))
save(4, sP5_20, "/scratch/li1.feng/BPS-spectra/star_5_20_P.csv")
save(4, sN5_20, "/scratch/li1.feng/BPS-spectra/star_5_20_N.csv")

r5_20 = [5] + [2000] * 5
sP5_20 = solveP(rangeall(r5_20))
sN5_20 = solveN(rangeall(r5_20))
save(6, sP5_20, "/scratch/li1.feng/BPS-spectra/solutions_5_2000_P_all.csv")
save(6, sN5_20, "/scratch/li1.feng/BPS-spectra/solutions_5_2000_N_all.csv")

r5_2000 = [5] + [2000]*5
sP5_2000 = s4P(rs4(r5_2000))
save(4, sP5_2000, "/scratch/li1.feng/BPS-spectra/star_5_2000_P.csv")
sN5_2000 = s4N(rs4(r5_2000))
save(4, sN5_2000, "/scratch/li1.feng/BPS-spectra/star_5_2000_N.csv")