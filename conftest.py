import pytest
from unittest.mock import Mock
from classes.bun import Bun
from classes.ingredient import Ingredient
from classes.ingredient_types import *
from helpers import *
import random as r


@pytest.fixture
def dummy_bun():
    m = Mock()
    m.get_name.return_value = "dummy"
    m.get_price.return_value = 1
    return m


@pytest.fixture
def dummy_ingredient():
    return create_dummy_ingredient_mock()


@pytest.fixture
def three_dummy_ingredients():
    return [create_dummy_ingredient_mock(), create_dummy_ingredient_mock(), create_dummy_ingredient_mock()]


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
