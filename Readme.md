# RoTools

Librería para simplificar el uso de [roboticstoolbox-python](https://pypi.org/project/roboticstoolbox-python/)

## Librerías necesarias

- roboticstoolbox-python
- numpy==1.26.4
- tabulate

```bash
pip install .
```

> [!WARNING]
> para versiones de Python **3.8** es necesario modificar el archivo de ansitable (`~/.local/lib/python3.8/site-packages/ansitable/table.py`) con [table.py](https://gist.github.com/adnksharp/c1f4dcfcec0f9f83c44d5c07d6d22f93)

## Funciones
* `getA`: Genera la matriz de rotación A.
* `getlinks`: Genera los links del [robot](https://petercorke.github.io/robotics-toolbox-python/arm_superclass.html#robot).
* `info`:Imprime lo que se ve en consola usando tabulate.

## Ejemplos

### Robot de planar con 2 articulaciones

![](https://i.imgur.com/0q2IaBw.png)

```shell
python3 example2D.py
```

<details>
<summary>

[example2D.py](example2D.py)

</summary>

```shell
ERobot: robot 2DOF, 2 joints (RR)
┌──────┬────────┬───────┬────────┬─────────────────────┐
│ link │  link  │ joint │ parent │ ETS: parent to link │
├──────┼────────┼───────┼────────┼─────────────────────┤
│    0 │ link0  │     0 │ BASE   │ Rz(q0)              │
│    1 │ link1  │     1 │ link0  │ tx(1) ⊕ Rz(q1)      │
│    2 │ @link2 │       │ link1  │ tx(1)               │
└──────┴────────┴───────┴────────┴─────────────────────┘

{}^{0}A_{f}:
  -0.1045   -0.9945    0         0.3955    
   0.9945   -0.1045    0         1.861     
   0         0         1         0         
   0         0         0         1         

Ángulos de Euler
┌─────┬─────┬─────────┐
│   φ │   θ │       ψ │
├─────┼─────┼─────────┤
│   0 │   0 │ 1.67552 │
└─────┴─────┴─────────┘

Cuaternión:
[ 0.6691 <<  0.0000,  0.0000,  0.7431 >> ]

q:
┌─────────┬──────────┐
│ 1.04716 │ 0.628392 │
└─────────┴──────────┘
``` 

</details>

### Robot de 3 articulaciones

![](https://i.imgur.com/s4byc90.png)

```shell
python3 example3D.py
```

<details>
<summary>

[example3D.py](example3D.py)

</summary>

```shell
ERobot: robot 3DOF, 3 joints (RRR)
┌──────┬────────┬───────┬────────┬──────────────────────────┐
│ link │  link  │ joint │ parent │   ETS: parent to link    │
├──────┼────────┼───────┼────────┼──────────────────────────┤
│    0 │ link0  │     0 │ BASE   │ tz(1) ⊕ Rz(q0)           │
│    1 │ link1  │     1 │ link0  │ tx(1) ⊕ Rx(90°) ⊕ Rz(q1) │
│    2 │ link2  │     2 │ link1  │ tx(1) ⊕ Rz(q2)           │
│    3 │ @link3 │       │ link2  │ tx(1) ⊕ Rx(-90°)         │
└──────┴────────┴───────┴────────┴──────────────────────────┘

{}^{0}A_{f}:
   0.2369   -0.866    -0.4403    1.141     
   0.4104    0.5      -0.7626    1.977     
   0.8806    0         0.4739    2.468     
   0         0         0         1         

Ángulos de Euler
┌─────────┬─────────┬──────────┐
│       φ │       θ │        ψ │
├─────────┼─────────┼──────────┤
│ -2.0944 │ 1.07712 │ -3.14159 │
└─────────┴─────────┴──────────┘

Cuaternión:
[ 0.7434 <<  0.2564, -0.4442,  0.4292 >> ]

q:
┌────────┬──────────┬──────────┐
│ 1.0472 │ 0.627495 │ 0.450159 │
└────────┴──────────┴──────────┘
``` 

</details>

## En proceso
> [!NOTE]
> Usar dos vectores `D` y `d` para separar transformaciones de eslabones, de juntas prismáticas..
