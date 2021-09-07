class Beverage:
    def __init__(self, beverage_name, all_ingredients):
        self.beverage_name = beverage_name
        self.ingredients = dict()
        for ingredient_name in all_ingredients:
            ingredient_quantity = all_ingredients[ingredient_name]
            self.ingredients[ingredient_name] = ingredient_quantity

    def add_ingredient(self, name, quantity):
        if quantity >= 0:
            self.ingredients[name] = quantity

    def get_ingredient_quantity(self, name):
        return self.ingredients.get(name, -1)

    def remove_ingredient(self, name):
        del self.ingredients[name]

    def get_beverage_name(self):
        return self.beverage_name

    def get_beverage_ingredients(self):
        return self.ingredients
