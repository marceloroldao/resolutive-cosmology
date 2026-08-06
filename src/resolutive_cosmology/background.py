"""Background-expansion reference models.

The Resolutive Cosmology equations will be added in a separate module after
formal specification. This file provides a transparent flat Lambda-CDM
reference implementation for numerical validation.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True, slots=True)
class FlatLambdaCDM:
    """Minimal flat Lambda-CDM background model.

    Parameters
    ----------
    h0:
        Hubble constant in km s^-1 Mpc^-1.
    omega_m:
        Present-day matter density parameter.
    omega_r:
        Present-day radiation density parameter.
    """

    h0: float = 70.0
    omega_m: float = 0.3
    omega_r: float = 0.0

    def __post_init__(self) -> None:
        if self.h0 <= 0.0:
            raise ValueError("h0 must be positive")
        if self.omega_m < 0.0 or self.omega_r < 0.0:
            raise ValueError("density parameters must be non-negative")
        if self.omega_m + self.omega_r > 1.0:
            raise ValueError("flat model requires omega_m + omega_r <= 1")

    @property
    def omega_lambda(self) -> float:
        """Present-day dark-energy density parameter."""
        return 1.0 - self.omega_m - self.omega_r

    def e(self, redshift: ArrayLike) -> NDArray[np.float64]:
        """Return the dimensionless expansion rate E(z) = H(z) / H0."""
        z = np.asarray(redshift, dtype=float)
        if np.any(z < 0.0):
            raise ValueError("redshift must be non-negative")
        return np.sqrt(
            self.omega_r * (1.0 + z) ** 4
            + self.omega_m * (1.0 + z) ** 3
            + self.omega_lambda
        )

    def hubble(self, redshift: ArrayLike) -> NDArray[np.float64]:
        """Return H(z) in km s^-1 Mpc^-1."""
        return self.h0 * self.e(redshift)
