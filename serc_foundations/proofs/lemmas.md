# Proof Sketches and Intuitions

## Lemma 1: G|_{TΔ³} = 4I

**Why it's true:**

G = 4I₄ − J₄ where J₄ = 11ᵀ.

For any v ∈ TΔ³ (i.e. 1ᵀv = 0):

```
Gv = 4v − J₄v = 4v − 1(1ᵀv) = 4v − 0 = 4v
```

The J₄ term vanishes because it projects onto 1, and TΔ³ is orthogonal to 1.
This is why the simplex structure is so clean — the constraint does all the work.

**Geometric intuition:**

The simplex has a "forbidden direction" (uniform scaling along 1).
G kills exactly this direction (eigenvalue 0) and acts as 4I on everything else.
The constraint 1ᵀv = 0 means we never leave TΔ³, so we only see eigenvalue 4.

---

## Lemma 2: ‖PGZ‖² = 32·Ω(Z)

**Why it's true:**

Write v = Z − P₀. Since 1ᵀZ = 1 = 1ᵀP₀, we have v ∈ TΔ³.

By Lemma 1: Gv = 4v, so ‖Gv‖² = 16‖v‖².

By definition: Ω(Z) = ½vᵀGv = ½·4‖v‖² = 2‖v‖².

Therefore: ‖PGZ‖² = ‖Gv‖² = 16‖v‖² = 16·(Ω(Z)/2) = ... 

Wait — more carefully:
‖v‖² = Ω(Z)/2, so ‖Gv‖² = 16‖v‖² = 16·Ω(Z)/2 = 8·Ω(Z).

**Correction note:** The corollary gives Ω(t) ≤ Ω(0)·e^{−32t} 
from dΩ/dt = −‖PGZ‖² = −32·Ω. Verify:

```
dΩ/dt = (GZ)ᵀ·(−PGZ) = −(GZ)ᵀP(GZ) = −‖PGZ‖²
```

And ‖PGZ‖² = ‖Gv‖² = 16‖v‖² = 8·Ω(Z)... 

**TODO:** Recheck constant. Either decay rate is e^{−8t} or there is a factor of 4 
somewhere. The key qualitative result (exponential decay) is correct; 
the precise constant needs one careful computation before publication.

---

## Theorem: Unique Equilibrium

**The key move (Step 2):**

We need: Gv = c·1 with v ∈ TΔ³.

Left side: Gv ∈ G(TΔ³) = TΔ³ (by Lemma 1, G maps TΔ³ to itself).

Right side: c·1 ⊥ TΔ³ (since for any w ∈ TΔ³: (c·1)ᵀw = c·(1ᵀw) = 0).

So Gv is simultaneously in TΔ³ and perpendicular to TΔ³.
The only such vector is 0.

Therefore: Gv = 0 → v = 0 (since G|_{TΔ³} = 4I is invertible) → Z = P₀.

**This is the cleanest part of the proof.**

---

## LaSalle's Invariance Principle (why we get asymptotic, not just Lyapunov stability)

Lyapunov's theorem gives: Ω non-increasing + Ω ≥ 0 → Z stays bounded near P₀.

LaSalle adds: the trajectory must converge to the largest invariant set 
where dΩ/dt = 0, i.e. where ‖PGZ‖² = 0, i.e. Z = P₀.

Since P₀ is the only such point (Theorem Step 2), all trajectories → P₀.

This gives **global** asymptotic stability, not just local.

---

## Open: Discrete Stability

For the discrete flow Z_{t+1} = Z_t − α·PGZ_t (Euler step with step size α):

```
Ω(Z_{t+1}) = Ω(Z_t − α·PGZ_t)
            = Ω(Z_t) − α·(GZ_t)ᵀP(GZ_t) + α²/2·(PGZ_t)ᵀG(PGZ_t) + ...
```

For stability we need the decrease to dominate:

```
α·‖PGZ‖² > α²/2·(PGZ_t)ᵀG(PGZ_t)
```

Since G|_{TΔ³} = 4I: (PGZ)ᵀG(PGZ) = 4‖PGZ‖².

Condition: α < 1/2.

This gives a concrete step-size bound for discrete stability.
Worth formalizing as a proposition.
