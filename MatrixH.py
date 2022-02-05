import numpy as np
import gauss
from scipy.ndimage.interpolation import rotate


class MatrixH:
    def __init__(self):
        self.H = np.zeros((4, 4))

    def calculate(self, jacob, ele4, conductivity, npc=2):
        for i in range(4):
            dNdX = [[], [], [], []]
            dNdY = [[], [], [], []]

            for x in range(4):
                for y in range(4):
                    dNdX[x].append(
                        jacob.jacob_inv[i][0][0] * ele4.ksi[x][y] + jacob.jacob_inv[i][1][0] * ele4.eta[x][y])
                    dNdY[x].append(
                        jacob.jacob_inv[i][0][1] * ele4.ksi[x][y] + jacob.jacob_inv[i][1][1] * ele4.eta[x][y])

            tempX = rotate(dNdX, 90)
            tempX = tempX[0:4, i:i + 1]
            tempX = rotate(tempX, 180)

            tempY = rotate(dNdY, 90)
            tempY = tempY[0:4, i:i + 1]
            tempY = rotate(tempY, 180)

            tempX = np.multiply(tempX, np.array(dNdX[i]))
            tempY = np.multiply(tempY, np.array(dNdY[i]))

            tempH = np.add(tempX, tempY)
            det = np.linalg.det(jacob.jacob[i])
            tempH = np.multiply(tempH, det * conductivity)
            self.H = np.add(tempH, self.H)

    def drawH(self):
        print("MACIERZ H")
        print(self.H.round(), end="\n\n")
