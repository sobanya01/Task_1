import pytest
from unittest.mock import Mock
import random as r


def create_dummy_ingredient_mock():
    m = Mock()
    m.get_name.return_value = f"dummy_name_{r.randint(0, 1000)}"
    m.get_price.return_value = 1
    m.get_type.return_value = "dummy_type"
    return m
