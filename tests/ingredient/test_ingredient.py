from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")

    assert ingredient == ingredient2
    assert ingredient != ingredient3
    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)

    assert repr(ingredient) == "Ingredient('queijo mussarela')"
    assert ingredient.name == "queijo mussarela"

    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
