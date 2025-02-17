from roboticstoolbox import Robot
from numpy import ndarray, array
from math import pi
from rotools import Nobot

if __name__ == '__main__':
    title = 'robot 3DOF'

    d: ndarray = array([1.0, 1.0, 1.0, 1.0])
    Q: ndarray = array([0.0, pi/2, 0.0, 0.0, -pi/2])
    q: ndarray = array([0.0, 0.0, 0.0])

    transform = [
            ['tz', 'Rz'],
            ['tx', 'Rx', 'Rz'],
            ['tx', 'Rz'],
            ['tx', 'Rx'],
        ]

    joint = ['R', 'R', 'R', None]

    lims = [
            [-pi, pi],
            [-pi, pi],
            [-pi, pi],
            [-pi, pi]
        ]

    nobot = Nobot(d, Q, q, transform, joint, lims)

    Aij = nobot.getA()

    links = nobot.getlinks(Aij)

    robot = Robot(links, name = title)
    q[0] = pi/3
    q[1] = pi/5
    q[2] = pi/7

    nobot.info(robot, q, 'robot', 'A', 'Euler', 'quat', 'q')
    # nobot.tab('\nq:', robot.ik_NR(robot.fkine(q))[0])

    try:
        robot.plot(q, block = True, backend = 'pyplot')
    except KeyboardInterrupt:
        exit(0)

