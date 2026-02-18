import numpy as np
from .serc import barycentric_project, coherence, grad_Q, P0, G

def update(Z, X, alpha=0.1, beta=0.05):
    Z = Z + alpha * X
    Z = Z - beta * grad_Q(Z)
    return barycentric_project(Z)

def simulate(steps=200, reset=False):
    Z = barycentric_project(np.random.rand(4))
    traj, Qvals = [], []
    T = 0.0

    for _ in range(steps):
        X = barycentric_project(np.random.rand(4))
        Z_new = update(Z, X)

        dZ = Z_new - Z
        v = np.sqrt(dZ @ G @ dZ)
        T += v

        Z = Z_new
        if reset:
            Z = P0.copy()

        traj.append(Z.copy())
        Qvals.append(coherence(Z))

    return np.array(traj), np.array(Qvals), T
