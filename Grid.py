class Node:
    def __init__(self, x, y, z, nr=0):
        self.nr = nr
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f"Node nr {self.nr}\n{self.x}, {self.y} | {self.z}", end="\n")


class Element:
    def __init__(self, nodes, nr):
        self.ID = nodes
        self.nr = nr
        self.H = None
        self.Hbc = None
        self.C = None
        self.P = None

    def draw(self):
        print("Element nr", self.nr)
        print(self.ID)


class Grid:
    def __init__(self):
        self.nodes = []
        self.elements = []

    def create(self, H, B, nH, nB):
        # Create nodes with boundary condition
        count = 1
        for i in range(nB):
            for j in range(nH):
                if ((i == 0) or (i == nB - 1)) or ((j == 0) or (j == nB - 1)):
                    self.nodes.append(Node(i / (nB - 1) * B, j / (nH - 1) * H, 1, count))
                else:
                    self.nodes.append(Node(i / (nB - 1) * B, j / (nH - 1) * H, 0, count))
                count += 1

        # Create elements
        for i in range(((nH - 1) * (nB - 1))):
            m = (i // (nB - 1)) + 1
            node1 = i + m
            node2 = i + nH + m
            node3 = i + nH + m + 1
            node4 = i + m + 1
            self.elements.append(Element([node1, node2, node3, node4], i + 1))

    def draw(self):
        print("ELEMENTS")
        for element in self.elements:
            element.draw()

        print("\n\nNODES")
        for node in self.nodes:
            node.draw()
        print()
