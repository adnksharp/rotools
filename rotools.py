from roboticstoolbox import ET, Link
from spatialmath import quaternion

from tabulate import tabulate

class Nobot():
    def __init__(self, d, Q, q, t, j, lims):
        self.d = d
        self.Q = Q
        self.q = q
        self.trans = t
        self.joints = j
        self.range = lims

    def getA(self):
        di, qi = 0, 0
        AIJ = []
        for i in range(len(self.trans)):
            for j in range(len(self.trans[i])):
                A = getattr(ET, self.trans[i][j])
                if 't' in self.trans[i][j]:
                    if self.d[di] != 0:
                        A: ET = A(self.d[di])
                    else:
                        A: ET = A()
                    di += 1
                else:
                    if self.Q[qi] != 0:
                        A: ET = A(self.Q[qi])
                    else:
                        A: ET = A()
                    qi += 1
                if j == 0:
                    AIJ.append(A)
                else:
                    AIJ[i] *= A
        return AIJ

    def getlinks(self, AIJ):
        links: Link =[]
        for i in range(len(AIJ)):
            l: Link = Link(
                AIJ[i],
                name = f'link{i}',
                qlim = self.range[i],
                parent = links [i - 1] if i > 0 else None,
                jindex = i,
                joint = self.joints[i]
            )
            links.append(l)
        return links
