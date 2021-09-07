1. Setup
To run this python3 file we only need to install python3 from https://www.python.org/downloads/ , if not already installed


2. Assumptions

The program assumes :
i. The input file is a valid json and has all information about coffee machine as well as beverages requested
ii. The input is not having duplicate ingredient entries
iii. We are not keeping track of requests which are missed in case, all available machines are in use

3. Available methods:

request_beverage : to request a specific beverage from coffee-machine

get_low_running_ingredients : to get a list of ingredients with lowest quantity eg [ (qt1,ing1) , (qt2,ing2) ]

refill_ingredients_in_inventory : method for adding / refilling a specific ingredient

check_and_update : method to check if for a specific beverage all necessary
                   ingredients are available in required quantity and based on that remove/deduct it from the inventory

initialize_inventory : method to initialize inventory with given ingredients and there respective quantities


4. Commands

To run the program , have an input json file ready like "coffee-machine-test-input.json"

then in the directory where "main.py" is present , run the command:

$ python3 main.py coffee-machine-test-input.json
