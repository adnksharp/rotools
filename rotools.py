from roboticstoolbox import ET, Link
from spatialmath import quaternion
from tabulate import tabulate

class Nobot():
    def __init__(self, d, Q, q, t, j, lims):
        """
Libreria para facilitar el uso de roboticstoolbox-python

Definicion del objeto de la libreria

Parametros
----------
d: numpy.ndarray
    Array de distancias de las traslaciones
Q: nupy.ndarray
    Array con todas las rotaciones de cada transformación
q: numpy.ndarray
    Array con los n valores de q
t: list
    Array con las transformaciones entre cada plano
j: list
    Array con los tipos de juntas del robot
lims: list
    Limites de cada junta

Retorno
-------
Nobot: class
    Objeto de la libreria

Ejemplo
-------
from numpy import ndarray, array
from rotools import Nobot

# Para un robot con tres traslaciones
d: ndarray = array([1.0, 1.0, 1.0, 1.0])

# Incluyendo la cantidad total del rotaciones del sistema
Q: ndarray = array([0.0, pi/2, 0.0, 0.0, -pi/2])

# Vector de q0, q1, ...
q: ndarray = array([0.0, 0.0, 0.0])

# array de transformaciones
transform = [
    ['tz', 'Rz'],           # Transformacion 0A1: Tx * Rz
    ['tx', 'Rx', 'Rz'],     # Transformacion 1A2: Tx * Rx * Rz
    ['tx', 'Rz'],           # Transformacion 2A3: Tx * Rz
    ['tx', 'Rx'],           # Transformacion 3A4: Tx * Rx
]

# juntas del robot 
joint = ['R', 'R', 'R', None]

# Limite de cada junta
lims = [
    [-pi, pi],
    [-pi, pi],
    [-pi, pi],
    [-pi, pi]
]

# objeto nobot
nobot = Nobot(d, Q, q, transform, joint, lims)
        """
        self.d = d
        self.Q = Q
        self.q = q
        self.trans = t
        self.joints = j
        self.range = lims

    def getA(self):
        """
        Obtiene la matriz de rotación A de 0 a f

        Parametros
        ----------
        Ninguno

        Retorno
        -------
        Aij: list
            Matriz de rotacion

        Ejemplo
        -------
        # revisar help(Nobot))
        A = Aij = nobot.getA()
        """
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
        """
        Obtiene los links del robot (necesarios para usar la instruccion Robot)

        Parametros
        ----------
        Aij: list
            Matriz de rotacion

        Retorno
        -------
        links: list
            LInks del robot

        Ejemplo
        -------
        # revisar help(Nobot))
        links = nobot.getlinks(Aij)
        """
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

    def tab(self, pre, data, title = None, style = 'simple_grid'):
        """"
        Imprime tablas usando tabulate (ansitable)

        Parametros
        ----------
        pre: str
            String a imprimir antes de la tabla
        data: list
            Vector de datos a imprimir en la tabla
        title: list
            Vector de strings para mostrar como encabezados
        style: str
            Estilo de la tabla
            https://github.com/astanin/python-tabulate?tab=readme-ov-file#table-format


        Retorno
        -------
        Vacio

        Ejemplo
        -------
        nobot.tab('\nq:', robot.ik_NR(robot.fkine(q))[0])
        """
        if pre:
            print(pre)
        if title:
            print(tabulate([data], headers = title, tablefmt = style))
        else:
            print(tabulate([data], tablefmt = style))

    def info(self, robot, q, *prints):
        """"
        Imprime información del robot

        Parametros
        ----------
        robot: roboticstoolbox.robot.Robot.Robot
            String a imprimir antes de la tabla
        q: numpy.ndarray
            Vector de datos a imprimir en la tabla
        *prints: str
            Cosas a imprimir
            'robot', 'A', 'Euler', 'quat', 'q'

        Retorno
        -------
        Vacio

        Ejemplo
        -------
        nobot.info(robot, q, 'robot', 'A', 'Euler', 'quat', 'q')
        """
        A = robot.fkine(q)

        for _ in prints:
            if 'robot' == _.lower():
                print(robot)
            if 'A' == _.upper():
                print('{}^{0}A_{f}:')
                print(A)
            if 'euler' == _.lower():
                self.tab('Ángulos de Euler', A.eul(), title = ['\u03C6','\u03B8','\u03C8'])
            if 'quat' in _.lower():
                print(f'\nCuaternión:\n[{A.UnitQuaternion()} ]')
            
            if 'q' == _.lower():
                self.tab('\nq:', robot.ik_NR(A)[0])
