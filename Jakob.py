import numpy as np

class Jakob:
    def __init__(self, element, nodes, ele4, npc):
        self.ele4 = ele4
        self.ID = element
        self.nodes = nodes
        self.jacob = []
        self.jacob_inv = []
        self.npc = npc

    def calculate(self):
        for x in range(self.npc**2):
            jakob = [[0, 0], [0, 0]]
            for y in range(4):
                jakob[0][0] += self.nodes[self.ID[y] - 1].x * self.ele4.ksi[x][y]
                jakob[0][1] += self.nodes[self.ID[y] - 1].x * self.ele4.eta[x][y]
                jakob[1][0] += self.nodes[self.ID[y] - 1].y * self.ele4.ksi[x][y]
                jakob[1][1] += self.nodes[self.ID[y] - 1].y * self.ele4.eta[x][y]
            self.jacob.append(jakob)
        self.jacob = np.array(self.jacob)
        self.jacob_inv = np.linalg.inv(self.jacob)

    def draw(self):
        print("\n\n<------------------------------------------------------------------->")
        print("ELEMENT")
        print(self.ID)
        print("\nJACOB")
        for x in self.jacob:
            print(x)

        print("\nINVERTED JACOB")
        for x in self.jacob_inv:
            print(x, end="\n\n")
