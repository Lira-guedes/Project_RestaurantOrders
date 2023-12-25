from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction 
import pytest


# Req 2
def test_dish():
    dish = Dish("picanha", 25.99)

    assert dish.name == "picanha"
    assert dish.price == 25.99

    assert dish.__repr__() == "Dish('picanha', R$25.99)"
    assert dish.__hash__() == hash("Dish('picanha', R$25.99)")
    assert dish.__eq__(Dish("picanha", 25.99)) is True

    with pytest.raises(TypeError):
        Dish("picanha", "25.99")

    with pytest.raises(ValueError):
        Dish("picanha", -25.99)
        
    ingredient = Ingredient("ovo")
    dish.add_ingredient_dependency(ingredient, 1)

    assert dish.recipe == {ingredient: 1}
    assert dish.get_ingredients() == {ingredient}
    assert dish.get_restrictions() == ingredient.restrictions

