import pytest

from classes.burger import Burger


class TestBurger:
    def test_create_burger_set_bun_correct(self, dummy_bun):
        b = Burger()
        b.set_buns(dummy_bun)
        assert b.bun.get_name() == dummy_bun.get_name()

    def test_burger_add_ingredient(self, dummy_ingredient):
        b = Burger()
        b.add_ingredient(dummy_ingredient)
        assert b.ingredients[0] == dummy_ingredient

    def test_burger_add_several_ingredients(self, dummy_ingredient):
        b = Burger()
        b.add_ingredient(dummy_ingredient)
        b.add_ingredient(dummy_ingredient)
        assert len(b.ingredients) == 2

    def test_burger_remove_ingredient(self, dummy_ingredient):
        b = Burger()
        b.add_ingredient(dummy_ingredient)
        b.remove_ingredient(0)
        assert len(b.ingredients) == 0

    def test_burger_move_ingredient(self, three_dummy_ingredients):
        b = Burger()

        one, two, three = three_dummy_ingredients

        b.add_ingredient(one)
        b.add_ingredient(two)
        b.add_ingredient(three)

        b.move_ingredient(0, 1)

        assert b.ingredients == [two, one, three]

    def test_burger_correct_price(self, dummy_bun, three_dummy_ingredients):
        b = Burger()
        b.set_buns(dummy_bun)

        one, two, three = three_dummy_ingredients

        b.add_ingredient(one)
        b.add_ingredient(two)
        b.add_ingredient(three)

        assert b.get_price() == 5

    def test_burger_correct_receipt(self, dummy_bun, three_dummy_ingredients):
        b = Burger()
        b.set_buns(dummy_bun)

        one, two, three = three_dummy_ingredients

        b.add_ingredient(one)
        b.add_ingredient(two)
        b.add_ingredient(three)

        assert b.get_receipt() == (
            f"(==== {dummy_bun.get_name()} ====)\n"
            f"= {one.get_type()} {one.get_name()} =\n"
            f"= {two.get_type()} {two.get_name()} =\n"
            f"= {three.get_type()} {three.get_name()} =\n"
            f"(==== {dummy_bun.get_name()} ====)\n\n"
            "Price: 5"
        )
