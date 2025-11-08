import pytest
from unittest.mock import Mock
from classes.bun import Bun
from classes.ingredient import Ingredient
from classes.ingredient_types import *
import random as r


@pytest.fixture
def dummy_bun():
    m = Mock()
    m.get_name.return_value = "dummy"
    m.get_price.return_value = 1
    return m


@pytest.fixture
def dummy_ingredient():
    m = Mock()
    m.get_name.return_value = f"dummy_name_{r.randint(0, 10)}"
    m.get_price.return_value = 1
    m.get_type.return_value = "dummy_type"
    return m


@pytest.fixture
def three_dummy_ingredients():
    one = Mock()
    one.get_name.return_value = f"dummy_name_{r.randint(0, 10)}"
    one.get_price.return_value = 1
    one.get_type.return_value = "dummy_type"

    two = Mock()
    two.get_name.return_value = f"dummy_name_{r.randint(0, 10)}"
    two.get_price.return_value = 1
    two.get_type.return_value = "dummy_type"

    three = Mock()
    three.get_name.return_value = f"dummy_name_{r.randint(0, 10)}"
    three.get_price.return_value = 1
    three.get_type.return_value = "dummy_type"
    return [one, two, three]


@pytest.fixture
def three_db_buns():
    return [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300),
    ]


@pytest.fixture
def database_ingredients():
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]
