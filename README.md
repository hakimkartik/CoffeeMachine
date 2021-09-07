# CoffeeMachine
Write the working code to create a working coffee machine with the desired features

1 . It will be serving some beverages. <br/>
2 . Each beverage will be made using some ingredients.  <br/>
3 . Assume time to prepare a beverage is the same for all cases.  <br/>
4 . The quantity of ingredients used for each beverage can vary. Also, the same ingredient (ex: water) can be used for multiple beverages.  <br/>
5 . There would be N ( N is an integer ) outlet from which beverages can be served.  <br/>
6 . Maximum N beverages can be served in parallel. <br/>
7 . Any beverage can be served only if all the ingredients are available in terms of quantity. <br/>
8 . There would be an indicator that would show which all ingredients are running low. We need some methods to refill them. <br/>

<br />
Input Test Json :- 
<br />

```
https://www.npoint.io/docs/77e0bf528e4af43cdc10
```

<br />
Expected Output :- 

Output 1
(This input can have multiple outputs. )
<br />
```
hot_tea is prepared
hot_coffee is prepared 
green_tea cannot be prepared because green_mixture is not available 
black_tea cannot be prepared because item hot_water is not sufficient
```
<br />

# Setup
To run this python3 file we only need to install python3 from https://www.python.org/downloads/ , if not already installed


# Assumptions

The program assumes :
* The input file is a valid json and has all information about coffee machine as well as beverages requested
* The input is not having duplicate ingredient entries
* We are not keeping track of requests which are missed in case, all available machines are in use

# Available methods:

`request_beverage` : to request a specific beverage from coffee-machine

`get_low_running_ingredients` : to get a list of ingredients with lowest quantity eg [ (qt1,ing1) , (qt2,ing2) ]

`refill_ingredients_in_inventory` : method for adding / refilling a specific ingredient

`check_and_update` : method to check if for a specific beverage all necessary
                   ingredients are available in required quantity and based on that remove/deduct it from the inventory

`initialize_inventory` : method to initialize inventory with given ingredients and there respective quantities


# Commands

To run the program , have an input json file ready like "coffee-machine-test-input.json"

then in the directory where "main.py" is present , run the command:

```
$ python3 main.py coffee-machine-test-input.json
```

Example : 

```
(venv) $ ls
beverage.py                     coffee_machine.py               main.py
coffee-machine-test-input.json  inventory.py                    venv
(venv) $ python3 main.py coffee-machine-test-input.json 
hot_tea is prepared
hot_coffee is prepared
black_tea cannot be prepared, hot_water is not sufficient
WARNING:root:black_tea was NOT prepared
green_tea cannot be prepared, sugar_syrup is not sufficient
WARNING:root:green_tea was NOT prepared
(venv) $ 

```
