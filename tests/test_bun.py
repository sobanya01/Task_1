import pytest
from classes.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", ["Рисовая", "Бриошь", " ", ""])
    def test_create_bun_returning_name_correct(self, name):
        b = Bun(name, 1.1)
        assert b.get_name() == name
        assert b.name == name

    @pytest.mark.parametrize("price", [0.0, 1.1, -1, 1])
    def test_create_bun_returning_price_correct(self, price):
        b = Bun("test", price)
        assert b.get_price() == price
        assert b.price == price
