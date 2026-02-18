import numpy as np
from .serc import G

def relational_velocity(Z1, Z2):
    dZ = Z2 - Z1
    return np.sqrt(dZ @ G @ dZ)

def relational_time(traj):
    T = 0.0
    for i in range(len(traj) - 1):
        T += relational_velocity(traj[i], traj[i+1])
    return T
