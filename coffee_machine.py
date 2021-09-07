from inventory import Inventory
from beverage import Beverage


class CoffeeMachineException(Exception):
    pass


class CoffeeMachine:
    # request_q = list() # can be used to queue up pending reuqests

    inventory = Inventory(None)  # static inventory manager object variable
    machine_in_use = 0  # static variable to keep track of num of coffee machines in use concurrently

    def __init__(self, num_of_machines):
        self.total_num_of_machines = num_of_machines

    def initialize_inventory(self, ingredients):
        self.inventory = Inventory(ingredients)

    def make_beverage(self, beverage_name, beverage_ingredients):
        """
        method to call inventory object and update if all beverage ingredients are present
        """
        beverage = Beverage(beverage_name, beverage_ingredients)
        status = self.inventory.check_and_update(beverage)
        return status

    def request_beverage(self, bvg_name, bvg_ingredients_data):
        """
        method to check if the passed beverage name is present in inventory
        and if its ingredients are present in necessary quantity
        """
        was_beverage_made = False
        if self.machine_in_use <= self.total_num_of_machines:
            self.machine_in_use += 1
            was_beverage_made = self.make_beverage(bvg_name, bvg_ingredients_data)
            self.machine_in_use -= 1
        else:
            raise CoffeeMachineException("Request cannot be processed yet as no machine is available")

        return was_beverage_made
