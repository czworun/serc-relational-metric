# SERC v2.0 – Technical Report

This directory contains the full implementation, experiments, and documentation for:

**SERC v2.0 – Geometry-Based Runtime Guardrail for LLMs**

SERC v2.0 introduces:
- the 4D relational mapper (S, E, R, C),
- L1 normalization instead of softmax,
- local drift D(t),
- independent coherence dimension C,
- the 3-signal adaptive guardrail,
- empirical validation on Qwen2.5-1.5B-Instruct.

## Structure

- `paper/` – PDF of the full technical report (SERC v2.0)
- `notebooks/` – NB1–NB3 used in the report
- `src/` – mapper v2, guardrail v2, utilities
- `calibration/` – calibration data for Qwen models

## Relation to the main SERC framework

This is the practical and experimental extension of the core SERC framework
located in the root of the repository. It provides the full implementation
and empirical validation of the relational geometry.

A mathematical supplement (SERC v2.1) is available in `../serc_foundations/`.
