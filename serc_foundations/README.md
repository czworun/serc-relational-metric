# SERC v2.1 – Mathematical Foundations

This directory contains the mathematical supplement to the SERC v2.0 technical report.

It formalizes the geometry of the SERC simplex and proves:

- the spectral structure of the Gram matrix G = 4I – J,
- the projected gradient flow on Δ³,
- Lyapunov stability of the relational equilibrium P₀ = (1/4,1/4,1/4,1/4),
- exponential relaxation rate Ω(t) = Ω(0) e^{-32t},
- interpretation of the ideal flow as a reference for LLM trajectory analysis.

## Structure

- `paper/` – PDF of the full mathematical supplement (SERC v2.1)
- `proofs/` – extended derivations and notes

## Relation to SERC v2.0

This document provides the theoretical foundation for the empirical work in `../serc_v2/`.

Where SERC v2.0 focuses on implementation and experiments,
SERC v2.1 establishes the underlying geometry and stability theory.
