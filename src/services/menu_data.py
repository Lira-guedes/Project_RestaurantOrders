from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path) -> None:
        self.dishes = set()
        self._menu_data(source_path)

    def _menu_data(self, source_path) -> None:
        with open(source_path, newline='') as csvfile:
            menu = csv.DictReader(csvfile)

            for row in menu:
                name = row['dish']
                price = float(row['price'])

                # Verifica se um prato com o mesmo nome e preço já existe
                dish = next((
                    dis for dis in self.dishes
                    if dis.name == name and dis.price == price
                ), None)

                # Se o prato não existir, cria um novo e adiciona ao conjunto
                if not dish:
                    dish = Dish(name, price)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(
                    Ingredient(row['ingredient']),
                    int(row['recipe_amount'])
                )
