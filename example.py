from numpy import ndarray, array
from roboticstoolbox import ET, Link, Robot
from spatialmath import quaternion
from math import pi
from tabulate import tabulate
from rotools import Nobot

if __name__ == '__main__':
    title = 'robot 2DOF'

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

    links = nobot.getlinks(Aij)

    robot = Robot(links, name = title)
    q[0] = pi/4
    q[1] = pi/4

    nobot.info(robot, q, 'robot', 'A', 'Euler', 'quat', 'q')

    try:
        robot.plot(q, block = True, backend = 'pyplot')
    except KeyboardInterrupt:
        exit(0)
"""
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
"""
