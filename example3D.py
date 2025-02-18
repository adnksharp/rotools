from roboticstoolbox import Robot
from numpy import ndarray, array
from math import pi
from rotools import Nobot

if __name__ == '__main__':
    # Nombre del robot
    title = 'robot 3DOF'

    # Variables de traslacion
    # distancia de moviminento d0, d1, ... de Ti0, Ti1, etc
    # 0 para usar variables simbolicas
    d: ndarray = array([1.0, 1.0, 1.0, 1.0])
    
    # Variables de rotacion
    # angulo de movimiento de Ri0, Ri1, ...
    # 0 para usar variables simbolicas
    # en este caso hay rotaciones en Rx que no pertenecen a juntas de rotacion
    # Q != q
    Q: ndarray = array([0.0, pi/2, 0.0, 0.0, -pi/2])
    # angulo de moviminento q0, q1, ... de Ri0, Ri1, etc
    # EXCLUSIVO PARA JUNTAS
    q: ndarray = array([0.0, 0.0, 0.0])

    # transformaciones del robot
    transform = [
            ['tz', 'Rz'],           #^0A1: Tz(d[0]) * Rx(q0)
            ['tx', 'Rx', 'Rz'],     #^1A2: Tx(d[1]) * Rx(q[1]) * Rz(q1)
            ['tx', 'Rz'],           #^2A3: Tx(d[2]) * Rz(q2)
            ['tx', 'Rx'],           #^3A4: Tx(d[3]) * Rx(q[3])
        ]

    # tipo de juntas
    joint = ['R', 'R', 'R', None]

    # limite de movimiento de cada junta
    lims = [
            [-pi, pi],
            [-pi, pi],
            [-pi, pi],
            [-pi, pi]
        ]

    # objeto de rotools.Nobot
    nobot = Nobot(d, Q, q, transform, joint, lims)

    # 1. Obtiene la matriz de transformacion ^0A_3
    # 2. Oobtiene los links del robot en base a la matriz de transformacion
    # 3. crea el robot roboticstoolbox.Robot con los links obtenidos
    robot = Robot(nobot.getlinks(nobot.getA()), name = title)
    
    # cambio de posicion del robot a j0: pi/3, j1 : pi/5
    q[0] = pi/3
    q[1] = pi/5
    q[2] = pi/7

    #imprime la informacion en la terminal
    nobot.info(robot, q, 'robot', 'A', 'Euler', 'quat', 'q')

    try:
        robot.plot(q, block = True, backend = 'pyplot')
    except KeyboardInterrupt:
        exit(0)

