from roboticstoolbox import Robot
from numpy import ndarray, array
from math import pi
from rotools import Nobot

if __name__ == '__main__':
    # Nombre del robot
    title = 'robot 2DOF'

    # Variables de traslacion
    # distancia de moviminento d0, d1, ... de Ti0, Ti1, etc
    d: ndarray = array([1.0, 1.0])
    
    # Variables de rotacion
    # angulo de movimiento de Ri0, Ri1, ...
    Q: ndarray = array([0.0, 0.0])
    # angulo de moviminento q0, q1, ... de Ri0, Ri1, etc
    # EXCLUSIVO PARA JUNTAS
    q: ndarray = array([0.0, 0.0])

    # transformaciones del robot
    transform = [
            ['Rz'],         #^0A_1: Rx(q0)
            ['tx', 'Rz'],   #^1A_2: Tx(d[1]) * Rz(q1)
            ['tx']          #^2A_3: Rx(d[2])
        ]

    # tipo de juntas
    joint = ['R', 'R', None]

    # limite de movimiento de las juntas
    lims = [
            [-pi, pi],  # lim inf, lim sup
            [-pi, pi],
            [-pi, pi]
        ]

    # objeto de rotools.Nobot
    nobot = Nobot(d, Q, q, transform, joint, lims)

    # obtiene la matriz de transformacion ^0A_3
    Aij = nobot.getA()

    # obtiene los links del robot 
    links = nobot.getlinks(Aij)

    # crea el robot roboticstoolbox.Robot
    robot = Robot(links, name = title)
    
    # cambio de posicion del robot a j0: pi/3, j1 : pi/5
    q[0] = pi/3
    q[1] = pi/5

    #imprime la informacion en la terminal
    nobot.info(robot, q, 'robot', 'A', 'Euler', 'quat', 'q')
    # nobot.tab('\nq:', robot.ik_NR(robot.fkine(q))[0])

    try:
        robot.plot(q, block = True, backend = 'pyplot')
    except KeyboardInterrupt:
        exit(0)

