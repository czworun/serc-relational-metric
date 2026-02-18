import numpy as np

# Gram matrix G = 4I - J
I = np.eye(4)
J = np.ones((4, 4))
G = 4 * I - J

P0 = np.array([0.25, 0.25, 0.25, 0.25])


def barycentric_project(Z):
    Z = np.maximum(Z, 0)
    s = np.sum(Z)
    return Z / s if s > 0 else P0.copy()


def coherence(Z):
    """Coherence functional Q(Z) = 1/2 Z^T G Z"""
    return 0.5 * Z @ G @ Z


def grad_Q(Z):
    """Gradient of Q: nabla Q = G Z"""
    return G @ Z
