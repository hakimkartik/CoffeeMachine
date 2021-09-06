import sys
import os
import json
from coffee_machine import CoffeeMachine


def file_sanity_check():
    file_data = None
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            with open(file_path) as file_ptr:
                file_data = json.load(file_ptr)
        else:
            print("{} not found".format(file_path))

    return file_data


def file_input():
    file_data = file_sanity_check()
    if file_data:
        machine_data = file_data["machine"]
        num_of_machine = machine_data['outlets']['count_n']
        total_ingredients = machine_data['total_items_quantity']
        list_of_beverages = machine_data['beverages']

        coffee_machines = CoffeeMachine(num_of_machine)
        coffee_machines.initialize_inventory(total_ingredients)

        for bvg_name in list_of_beverages:
            bvg_ingredients_data = machine_data['beverages'][bvg_name]
            coffee_machines.request_beverage(bvg_name, bvg_ingredients_data)


def main():
    file_input()


if __name__ == "__main__":
    main()
