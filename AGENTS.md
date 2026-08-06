# AGENTS.md

## Project mission
Build a reproducible, auditable computational framework for testing Resolutive Cosmology against ΛCDM.

## Rules for AI agents
1. Do not change a physical equation without documenting the mathematical and scientific reason.
2. Keep Resolutive Cosmology and ΛCDM implementations separate.
3. Use identical datasets, priors, likelihoods, and metrics in model comparisons.
4. Distinguish hypotheses, implemented models, numerical results, and scientific conclusions.
5. Add or update tests for every change in physical or numerical behavior.
6. Preserve units explicitly and reject ambiguous inputs.
7. Fix random seeds in reproducibility workflows.
8. Generate results only through versioned scripts or notebooks.
9. Do not present phenomenological fits as established physical discoveries.
10. Run the test suite before opening or updating a pull request.

## Architecture
- `src/resolutive_cosmology/`: package code
- `tests/`: unit and regression tests
- `docs/`: theory, assumptions, and validation protocol
- `notebooks/`: reproducible analyses only
- `data/`: metadata and acquisition instructions; avoid committing restricted datasets
- `results/`: generated tables and figures

## Coding standards
- Python 3.11+
- Type hints for public functions
- NumPy-style docstrings
- SI units by default
- Pure functions where practical
- No hidden global parameters
