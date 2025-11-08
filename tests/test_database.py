import pytest
from classes.database import Database


class TestDatabase:
    def test_database_check_buns(self, three_db_buns):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        black, white, red = buns

        assert black.get_name() == three_db_buns[0].get_name()
        assert white.get_name() == three_db_buns[1].get_name()
        assert red.get_name() == three_db_buns[2].get_name()

    def test_database_check_ingredients(self, database_ingredients):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

        assert ingredients[0].get_name() == database_ingredients[0].get_name()
        assert ingredients[1].get_name() == database_ingredients[1].get_name()
        assert ingredients[2].get_name() == database_ingredients[2].get_name()
        assert ingredients[3].get_name() == database_ingredients[3].get_name()
        assert ingredients[4].get_name() == database_ingredients[4].get_name()
        assert ingredients[5].get_name() == database_ingredients[5].get_name()
