import numpy as np

import data
from Element4 import Element4
from Jakob import Jakob
from Grid import Grid
from MatrixH import MatrixH
from MatrixHbc import MatrixHbc
from MatrixP import MatrixP
from MatrixC import MatrixC
from Agregate import agregateC, agregateH, agregateHbc, agregateP
from SolveTemp import calculateTemp
from data import *


def MES():
    # Approximation
    rounded = 4

    # Creating grid
    grid = Grid()
    grid.create(data.H, data.B, data.nH, data.nB)
    # grid.draw()

    # Calculating ksi and eta
    ele4 = Element4()
    ele4.calculate(npc)
    # ele4.draw()

    # Calculating every matrix for each element
    for element in grid.elements:
        # Calculate Jakob
        jakob = Jakob(element.ID, grid.nodes, ele4, npc)
        jakob.calculate()
        # Calculate H
        H = MatrixH()
        H.calculate(jakob, ele4, data.conductivity, data.npc)
        element.H = H.H
        # Calculate Hbc
        Hbc = MatrixHbc()
        Hbc.calculate(element, grid.nodes, data.alpha)
        element.Hbc = Hbc.Hbc
        # Calculate P
        P = MatrixP()
        P.calculate(element, grid.nodes, data.aT, data.alpha)
        element.P = P.P
        # Calculate C
        C = MatrixC()
        C.calculate(jakob, ele4, data.ro, data.cp, data.npc)
        element.C = C.C

        # # Draw each matrix
        # jakob.draw()
        # H.drawH()
        # print(element.ID)
        # Hbc.draw()
        # P.draw()
        # C.draw()

    H_agr = agregateH(grid)
    Hbc_agr = agregateHbc(grid)
    P_agr = agregateP(grid)
    P_agr = np.reshape(P_agr, (len(grid.nodes), 1))
    C_agr = agregateC(grid)

    print("\nMATRIX H AGGRAGATED")
    for x in np.ndarray.tolist(H_agr):
        x = [round(num, rounded) for num in x]
        print(x)

    print("\nMATRIX Hbc AGGRAGATED")
    for x in np.ndarray.tolist(Hbc_agr):
        x = [round(num, rounded) for num in x]
        print(x)

    print("\nMATRIX P AGGRAGATED")
    for x in np.ndarray.tolist(P_agr):
        x = [round(num, rounded) for num in x]
        print(x)

    print("\nMATRIX C AGGRAGATED")
    for x in np.ndarray.tolist(C_agr):
        x = [round(num, rounded) for num in x]
        print(x)

    print("\nTemperatura")
    # solved = SolveTemp(len(grid.nodes), P_agr, C_agr, H_agr, Hbc_agr)
    # solved.calculate()
    calculateTemp(len(grid.nodes), P_agr, C_agr, H_agr, Hbc_agr)


if __name__ == '__main__':
    MES()
