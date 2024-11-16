import sympy
import numpy as np
from scipy import optimize
import math
from math import pi
np.set_printoptions(
    linewidth=120, formatter={
        'float': lambda x: f"{0:8.4g}" if abs(x) < 1e-10 else f"{x:8.4g}"})
np.random.seed(0)
from spatialmath import *
from spatialmath.base import *
from roboticstoolbox import *


def compute_robot_angles(x: float, y: float, a0: float = 1, a1: float = 1) -> tuple[float]:
    """
    calculo de los angulos de un brazo robotico dado un punto (x, y)
    y la longitud de sus eslabones (a0, a1)
    """
    # definir variables simbolicas
    x_sym, y_sym = sympy.symbols("x, y")    # posicion efector final
    a0_sym, a1_sym = sympy.symbols("a0 a1") # longitudes de eslabones
    q0_sym, q1_sym = sympy.symbols("q0 q1") # angulos del brazo
    
    # definir la ecuacion simbolica del movimiento (modelo cinematico)
    kin_model = ET2.R() * ET2.tx(a0_sym) * ET2.R() * ET2.tx(a1_sym)

    # hallar ecuaciones de transformacion de la cinematica directa
    transform_eq = kin_model.fkine([q0_sym, q1_sym])
    x_fk, y_fk = transform_eq.t

    # hallar ecuaciones para los angulos    
    eq0 = tuple(map(sympy.expand_trig, [x_fk - x_sym, y_fk - y_sym]))
    eq1 = (x_fk**2 + y_fk**2-x_sym**2-y_sym**2).trigsimp()

    # resolver ecuaciones de los angulos
    q0_sol = sympy.solve(eq0, [sympy.sin(q0_sym), sympy.cos(q0_sym)])
    q1_sol = sympy.solve(eq1, q1_sym)
    q0_sol2 = sympy.atan2(q0_sol[sympy.sin(q0_sym)], q0_sol[sympy.cos(q0_sym)]).simplify()

    # substituir variables simbolicas y evaluar valores numericos
    q1_sol_subs = q1_sol[1].subs({x_sym:x, y_sym:y, a0_sym:a0, a1_sym:a1})
    q1_num = q1_sol_subs.evalf()
    q0_sol_subs = q0_sol2.subs({x_sym:x, y_sym:y, a0_sym:a0, a1_sym:a1, q1_sym:q1_num})
    q0_num = q0_sol_subs.evalf()
    print(f"Q0: {q0_num}, Q1: {q1_num}")
    return float(q0_num), float(q1_num)

def compute_end_effector(q0:float, q1:float, a0:float = 1, a1:float = 1) -> tuple[float]:
    # definir variables simbolicas
    a0_sym, a1_sym = sympy.symbols("a0 a1") # longitudes de eslabones
    q0_sym, q1_sym = sympy.symbols("q0 q1") # angulos del brazo

    # definir la ecuacion simbolica del movimiento (modelo cinematico)
    kin_model = ET2.R() * ET2.tx(a0_sym) * ET2.R() * ET2.tx(a1_sym)
    
    # hallar ecuaciones de transformacion de la cinematica directa
    transform_eq = kin_model.fkine([q0_sym, q1_sym])
    x_fk, y_fk = transform_eq.t

    # substituir variables simbolicas y evaluar valores numericos
    x_fk_sub = x_fk.subs({a0_sym:a0, a1_sym:a1, q0_sym:q0, q1_sym:q1})
    x_num = x_fk_sub.evalf()
    y_fk_sub = y_fk.subs({a0_sym:a0, a1_sym:a1, q0_sym:q0, q1_sym:q1})
    y_num = y_fk_sub.evalf()
    return float(x_num), float(y_num)


def compute_positions(q0: float, q1: float, a0: float = 1, a1: float = 1) -> list[tuple[float]]:
    end_effector_pos = compute_end_effector(q0, q1, a0, a1)
    x0 = a0 * math.cos(q0)
    y0 = a0 * math.sin(q0)

    return [(0, 0),(x0, y0), end_effector_pos]



    



