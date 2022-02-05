import numpy as np
import data


def calculateTemp(size, P_agr, C_agr, H_agr, Hbc_agr):
    dT = 0
    H_Hbc = np.add(H_agr, Hbc_agr)
    t0 = np.full((size, 1), data.initT)
    for i in range(data.simTime // data.simStep):
        dT += data.simStep

        finalH = np.multiply(C_agr, 1 / data.simStep)
        finalH = np.add(finalH, H_Hbc)

        finalP = np.multiply(C_agr, 1 / data.simStep)
        finalP = np.matmul(finalP, t0)
        finalP = np.add(finalP, P_agr)

        solved = np.linalg.solve(finalH, finalP)
        t0 = solved
        min_temp = np.min(solved)
        max_temp = np.max(solved)

        print("{}\t| min - {}\t| max - {}".format(dT, round(min_temp, 3), round(max_temp, 3)))
