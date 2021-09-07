import heapq


class InventoryException(Exception):
    pass


class Inventory:
    ingredient_vs_quantity = dict()

    def __init__(self, all_ingredients):
        self.ingredient_vs_quantity_heap = list()
        if isinstance(all_ingredients, dict):
            self.ingredient_vs_quantity = all_ingredients
            self.__update_ingredients_heap()

    def clear_inventory(self):
        self.ingredient_vs_quantity = None

    def _update_inventory(self, remove_quantities_from_inventory=None):
        for bev_name in remove_quantities_from_inventory:
            bev_quantity = remove_quantities_from_inventory[bev_name]
            self.ingredient_vs_quantity[bev_name] -= bev_quantity

    def __update_ingredients_heap(self):
        if not self.__is_inventory_initialized():
            raise InventoryException("Tried to update inventory but initialize inventory first... ")

        self.ingredient_vs_quantity_heap = []

        for ingredient in self.ingredient_vs_quantity:
            quantity = self.ingredient_vs_quantity[ingredient]
            heapq.heappush(self.ingredient_vs_quantity_heap, (quantity, ingredient))

    def add_ingredient_to_inventory(self, name, quantity):
        if quantity >= 0:
            self.ingredient_vs_quantity[name] = quantity
            heapq.heappush(self.ingredient_vs_quantity_heap, (quantity, name))

    def get_low_running_ingredients(self, n=None):
        """ method to get ingredients with lowest quantity """
        if not self.__is_inventory_initialized():
            raise InventoryException("Tried to read inventory but initialize inventory first... ")

        if n and isinstance(n, int):
            return heapq.nsmallest(n, self.ingredient_vs_quantity_heap)
        else:
            return list(self.ingredient_vs_quantity_heap)

    def refill_ingredients_in_inventory(self, name, quantity):
        if not self.__is_inventory_initialized():
            raise InventoryException("Tried to refill inventory but initialize inventory first... ")

        if quantity >= 0:
            self.ingredient_vs_quantity[name] += quantity
            self.__update_ingredients_heap()

    def get_quantity_in_inventory(self, ingredient_name):
        return self.ingredient_vs_quantity.get(ingredient_name, -1)

    def __is_inventory_initialized(self):
        return bool(self.ingredient_vs_quantity)

    def check_and_update(self, beverage):
        """
        method to gather info using passed beverage object and
        based on that update inventory if all necessary quantity is present
        """
        if not self.__is_inventory_initialized():
            raise InventoryException("Tried to make a beverage but initialize inventory first... ")

        status = True

        beverage_name = beverage.get_beverage_name()
        beverage_ingredients_quantity_mapping = beverage.get_beverage_ingredients()
        remove_quantities_from_inventory = dict()
        for beverage_ingredient in beverage_ingredients_quantity_mapping:
            quantity_needed_for_bvg = beverage_ingredients_quantity_mapping.get(beverage_ingredient, -1)
            # quantity_needed_for_bvg = beverage.get_ingredient_quantity(beverage_ingredient)
            quantity_in_inventory = self.get_quantity_in_inventory(beverage_ingredient)

            if quantity_in_inventory == -1:
                print("{} cannot be prepared, {} is finished".format(beverage_name, beverage_ingredient))
                status = False
                break

            elif quantity_in_inventory >= quantity_needed_for_bvg:
                remove_quantities_from_inventory[beverage_ingredient] = quantity_needed_for_bvg

            elif quantity_in_inventory < quantity_needed_for_bvg:
                print("{} cannot be prepared, {} is not sufficient".format(beverage_name, beverage_ingredient))
                status = False
                break

        if status:
            # removing here so that in case all ingredients are not available , wont mess up inventory then
            self._update_inventory(remove_quantities_from_inventory)
            self.__update_ingredients_heap()
            print("{} is prepared".format(beverage_name))

        return status
