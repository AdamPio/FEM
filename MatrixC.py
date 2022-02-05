import numpy as np
import gauss
import data


class MatrixC:
    def __init__(self):
        self.C = np.zeros((4, 4))

    def calculate(self, jakob, ele4, ro, cp, npc):
        for x in range(4):
            N = [0, 0, 0, 0]
            N[0] = 0.25 * (1 - ele4.P[x][0]) * (1 - ele4.P[x][1])
            N[1] = 0.25 * (1 + ele4.P[x][0]) * (1 - ele4.P[x][1])
            N[2] = 0.25 * (1 + ele4.P[x][0]) * (1 + ele4.P[x][1])
            N[3] = 0.25 * (1 - ele4.P[x][0]) * (1 + ele4.P[x][1])
            temp1 = np.array(N).reshape(4, 1)
            temp2 = np.array(N)
            N = np.multiply(temp1, temp2)
            det = np.linalg.det(jakob.jacob[0])
            N = np.multiply(N, ro * cp * det)
            self.C = np.add(self.C, N)

    def draw(self):
        print("MACIERZ C")
        print(self.C, end="\n\n")
