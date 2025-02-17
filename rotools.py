from roboticstoolbox import ET, Link
from spatialmath import quaternion

from tabulate import tabulate

class nobot():
    def __init(self, d, Q, q, t, j, lims):
        self.d = d
        self.Q = Q
        self.q = q
        self.t = t
        self.joints = j
        self.range = lims
