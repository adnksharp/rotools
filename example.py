from numpy import ndarray, array
from roboticstoolbox import ET, Link, Robot
from spatialmath import quaternion
from math import pi
from tabulate import tabulate
from rotools import Nobot

if __name__ == '__main__':
    """
   a0: float = 1.0
   d1: float = 1.0
   d2: float = 1.0
   d3: float = 1.0
   q1: float = 0.0
   q2: float = 0.0
   q3: float =0.0
    """
    d: ndarray = array([1.0, 1.0])
    Q: ndarray = array([0.0, 0.0])
    q: ndarray = array([0.0, 0.0])

    transform = [
            ['Rz'],
            ['tx', 'Rz'],
            ['tx'],
    ]

    joint = [ 'R', 'R', None ]

    lims = [
        [-pi, pi],
        [-pi, pi],
        [-pi, pi]
    ]

    nobot = Nobot(d, Q, q, transform, joint, lims)

    Aij = nobot.getA()
"""
   A01: ET = ET.tz(a0) * ET.Rz()
   A12: ET = ET.tx(d1) * ET.Rx(pi/2) * ET.Rz()
   A23: ET = ET.tx(d2) * ET.Rz()
   A3f: ET = ET.tx(d3) * ET.Rx(-pi/2)
 
   link0:Link = Link(A01,name='link0',qlim=[-pi,pi], parent=None,jindex=0,joint='R')
   link1:Link = Link(A12,name='link1',qlim=[-pi,pi], parent=link0,jindex=1,joint='R')
   Link2:Link = Link(A23,name='link2',qlim=[-pi,pi], parent=link1,jindex=2,joint='R')
   ef: Link = Link(A3f, name = 'ef', parent = Link2)
 
 
   links: Link = [link0, link1,Link2,ef]

   robot: Robot = Robot(links,name = '3dof')
   print(robot)
 
   q[0] = pi/4
   q[1] = pi/4
   q[2] = pi/4
 
   A = robot.fkine(q)
   print(A)
   phi, theta, psi = A.eul()
   print(tabulate([A.eul()], headers = ['phi', 'theta', 'psi'], tablefmt = 'simple_grid'))
   quat: quaternion.UnitQuaternion = A.UnitQuaternion()
   print(f'\nquat = {quat}')
   sol: tuple = robot.ik_NR(A)[0]
   print(f'\nq = {sol}')
   try:
        robot.plot(q, block = True, backend = 'pyplot')
   except KeyboardInterrupt:
        exit(0)
"""
