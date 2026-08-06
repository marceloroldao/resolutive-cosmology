import numpy as np
import pytest

from resolutive_cosmology import FlatLambdaCDM


def test_present_expansion_rate_equals_h0() -> None:
    model = FlatLambdaCDM(h0=67.4, omega_m=0.315)
    assert model.hubble(0.0) == pytest.approx(67.4)
    assert model.e(0.0) == pytest.approx(1.0)


def test_expansion_rate_increases_with_redshift() -> None:
    model = FlatLambdaCDM()
    values = model.hubble(np.array([0.0, 0.5, 1.0, 2.0]))
    assert np.all(np.diff(values) > 0.0)


def test_negative_redshift_is_rejected() -> None:
    model = FlatLambdaCDM()
    with pytest.raises(ValueError, match="redshift"):
        model.hubble(-0.1)


def test_invalid_density_parameters_are_rejected() -> None:
    with pytest.raises(ValueError, match="flat model"):
        FlatLambdaCDM(omega_m=0.9, omega_r=0.2)
