import numpy as np
import data

class SolveTemp():
    def __init__(self, size, P_agr, C_agr, H_agr, Hbc_agr,):
        self.size = size
        self.P_agr = P_agr
        self.C_agr = C_agr
        self.HHBC = np.add(H_agr, Hbc_agr)
        self.T0 = np.full((size, 1), data.initT)
        self.dT = 0

    def calculate(self):
        for i in range(data.simTime//data.simStep):
            self.dT += data.simStep

            finalH = np.multiply(self.C_agr, 1/data.simStep)
            finalH = np.add(finalH, self.HHBC)

            finalP = np.multiply(self.C_agr, 1/data.simStep)
            finalP = np.matmul(finalP, self.T0)
            finalP = np.add(finalP, self.P_agr)

            solved = np.linalg.solve(finalH, finalP)
            self.T0 = solved
            min_temp = np.min(solved)
            max_temp = np.max(solved)

            print("{}\t| min - {}\t| max - {}".format(self.dT, round(min_temp, 3), round(max_temp, 3)))