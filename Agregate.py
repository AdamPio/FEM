import numpy as np

def agregateC(grid):
    Cagr = np.zeros((len(grid.nodes), len(grid.nodes)))
    for element in grid.elements:
        for x in range(4):
            for y in range(4):
                if element.C is not None:
                    Cagr[element.ID[x] - 1][element.ID[y] - 1] += element.C[x][y]
    return Cagr


def agregateH(grid):
    Hagr = np.zeros((len(grid.nodes), len(grid.nodes)))
    for element in grid.elements:
        for x in range(4):
            for y in range(4):
                if element.H is not None:
                    Hagr[element.ID[x] - 1][element.ID[y] - 1] += element.H[x][y]
    return Hagr


def agregateHbc(grid):
    HBCagr = np.zeros((len(grid.nodes), len(grid.nodes)))
    for element in grid.elements:
        for x in range(4):
            for y in range(4):
                if element.Hbc is not None:
                    HBCagr[element.ID[x] - 1][element.ID[y] - 1] += element.Hbc[x][y]
    return HBCagr


def agregateP(grid):
    Pagr = np.zeros((len(grid.nodes)))
    for element in grid.elements:
        for x in range(4):
            if element.P is not None:
                Pagr[element.ID[x] - 1] += element.P[x]
    return Pagr
