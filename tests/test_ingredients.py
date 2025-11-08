import pytest
from classes.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("name", ["чесночный", "кетчуп", ""])
    def test_create_ingredient_returning_name_correct(self, name):
        i = Ingredient("соус", name, 1.0)
        assert i.name == name
        assert i.get_name() == name

    @pytest.mark.parametrize("type", ["соус", "начинка", ""])
    def test_create_ingredient_returning_type_correct(self, type):
        i = Ingredient(type, "test", 1.0)
        assert i.type == type
        assert i.get_type() == type

    @pytest.mark.parametrize("price", [1.0, 0.0, -1, 1])
    def test_create_ingredient_returning_price_correct(self, price):
        i = Ingredient("test", "test", price)
        assert i.price == price
        assert i.get_price() == price
