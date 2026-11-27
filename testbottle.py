import pytest
from production import calculate_material


def test_material_calculation():
    assert calculate_material(1000, 20) == 20


def test_small_production():
    assert calculate_material(100, 10) == 1


def test_large_production():
    assert calculate_material(5000, 50) == 250


def test_fractional_material():
    assert calculate_material(100, 12.5) == 1.25


def test_zero_bottles():
    with pytest.raises(ValueError):
        calculate_material(0, 20)