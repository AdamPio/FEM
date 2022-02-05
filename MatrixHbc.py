import numpy as np


class MatrixHbc:
    def __init__(self):
        self.Hbc = np.zeros((4, 4))
        self.Pc1 = [(-1 / np.sqrt(3), -1), (1 / np.sqrt(3), -1)]
        self.Pc2 = [(-1, -1 / np.sqrt(3)), (-1, 1 / np.sqrt(3))]
        self.Pc3 = [(-1 / np.sqrt(3), 1), (1 / np.sqrt(3), 1)]
        self.Pc4 = [(1, 1 / np.sqrt(3)), (1, -1 / np.sqrt(3))]

    def calculate(self, element, nodes, alpha=25, npc=2):

        Pc = 0
        for i in range(-1, 3):
            if i == -1:
                Pc = self.Pc2
            elif i == 0:
                Pc = self.Pc1
            elif i == 1:
                Pc = self.Pc4
            elif i == 2:
                Pc = self.Pc3
            if nodes[element.ID[i] - 1].z != 0 and nodes[element.ID[i + 1] - 1].z != 0:
                # print(element.ID[i], element.ID[i + 1])
                if np.abs(nodes[element.ID[i] - 1].x - nodes[element.ID[i + 1] - 1].x) != 0:
                    detJ = (np.abs(nodes[element.ID[i] - 1].x - nodes[element.ID[i + 1] - 1].x))/2
                else:
                    detJ = (np.abs(nodes[element.ID[i] - 1].y - nodes[element.ID[i + 1] - 1].y))/2
                N1 = [0, 0, 0, 0]
                N2 = [0, 0, 0, 0]

                N1[0] = 0.25 * (1 - Pc[1][0]) * (1 - Pc[1][1])
                N1[1] = 0.25 * (1 + Pc[1][0]) * (1 - Pc[1][1])
                N1[2] = 0.25 * (1 + Pc[1][0]) * (1 + Pc[1][1])
                N1[3] = 0.25 * (1 - Pc[1][0]) * (1 + Pc[1][1])
                N1 = np.asarray(N1)
                _N1 = N1
                _N1 = np.reshape(_N1, (4, 1))
                N1 = np.multiply(N1, _N1) * alpha

                N2[0] = 0.25 * (1 - Pc[0][0]) * (1 - Pc[0][1])
                N2[1] = 0.25 * (1 + Pc[0][0]) * (1 - Pc[0][1])
                N2[2] = 0.25 * (1 + Pc[0][0]) * (1 + Pc[0][1])
                N2[3] = 0.25 * (1 - Pc[0][0]) * (1 + Pc[0][1])
                N2 = np.asarray(N2)
                _N2 = N2
                _N2 = np.reshape(_N2, (4, 1))
                N2 = np.multiply(N2, _N2) * alpha

                self.Hbc += np.add(N1, N2) * detJ

    def draw(self):
        print("MACIERZ Hbc")
        print(self.Hbc, end="\n\n")
