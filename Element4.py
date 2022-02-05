import math

class Element4:

    def __init__(self):
        self.eta = []
        self.ksi = []
        self.P = None

    def calculate(self, npc):
        rounded = 6
        if npc == 2:
            a = math.sqrt(3) / 3
            for i in range(npc ** 2):
                self.ksi.append([])
                self.eta.append([])
            self.P = [(-a, -a), (a, -a), (a, a), (-a, a)]

        for i in range(len(self.P)):
            self.ksi[i].append(round(-1 / 4 * (1 - self.P[i][1]), rounded))
            self.ksi[i].append(round(1 / 4 * (1 - self.P[i][1]), rounded))
            self.ksi[i].append(round(1 / 4 * (1 + self.P[i][1]), rounded))
            self.ksi[i].append(round(-1 / 4 * (1 + self.P[i][1]), rounded))

            self.eta[i].append(round(-1 / 4 * (1 - self.P[i][0]), rounded))
            self.eta[i].append(round(-1 / 4 * (1 + self.P[i][0]), rounded))
            self.eta[i].append(round(1 / 4 * (1 + self.P[i][0]), rounded))
            self.eta[i].append(round(1 / 4 * (1 - self.P[i][0]), rounded))

    def draw(self):
        print("KSI")
        for array in self.ksi:
            for x in array:
                print(x, end=" ")
            print()

        print("\nETA")
        for array in self.eta:
            for x in array:
                print(x, end=" ")
            print()
