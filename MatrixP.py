import numpy as np

class MatrixP():
    def __init__(self):
        self.P = np.zeros((4, 1))
        self.Pc1 = [(-1 / np.sqrt(3), -1), (1 / np.sqrt(3), -1)]
        self.Pc2 = [(-1, -1 / np.sqrt(3)), (-1, 1 / np.sqrt(3))]
        self.Pc3 = [(-1 / np.sqrt(3), 1), (1 / np.sqrt(3), 1)]
        self.Pc4 = [(1, 1 / np.sqrt(3)), (1, -1 / np.sqrt(3))]

    def calculate(self, element, nodes, temp, alpha):
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
                if np.abs(nodes[element.ID[i] - 1].x - nodes[element.ID[i + 1] - 1].x) != 0:
                    detJ = (np.abs(nodes[element.ID[i] - 1].x - nodes[element.ID[i + 1] - 1].x))/2
                else:
                    detJ = (np.abs(nodes[element.ID[i] - 1].y - nodes[element.ID[i + 1] - 1].y))/2
                N1 = [0, 0, 0, 0]
                N2 = [0, 0, 0, 0]

                N1[0] = 0.25 * (1 - Pc[0][0]) * (1 - Pc[0][1])
                N1[1] = 0.25 * (1 + Pc[0][0]) * (1 - Pc[0][1])
                N1[2] = 0.25 * (1 + Pc[0][0]) * (1 + Pc[0][1])
                N1[3] = 0.25 * (1 - Pc[0][0]) * (1 + Pc[0][1])
                N1 = np.asarray(N1)
                N1 = np.reshape(N1, (4, 1))

                N2[0] = 0.25 * (1 - Pc[1][0]) * (1 - Pc[1][1])
                N2[1] = 0.25 * (1 + Pc[1][0]) * (1 - Pc[1][1])
                N2[2] = 0.25 * (1 + Pc[1][0]) * (1 + Pc[1][1])
                N2[3] = 0.25 * (1 - Pc[1][0]) * (1 + Pc[1][1])
                N2 = np.asarray(N2)
                N2 = np.reshape(N2, (4, 1))

                self.P += ((N1*temp)+(N2*temp))*alpha*detJ
        self.P = np.reshape(self.P, 4)

    def draw(self):
        print("MACIERZ P")
        print(self.P, end="\n\n")