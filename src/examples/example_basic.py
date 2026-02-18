from src.simulation import simulate

traj, Qvals, T = simulate(steps=100, reset=True)

print("Mean Q:", Qvals.mean())
print("Relational time:", T)
