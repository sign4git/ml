MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO 1. Ask user for an input
def coffee_user_interface():
    user_input = ""
    while user_input != "off":
        user_input = input(f"What would you like? (espresso/latte/cappuccino): ")
        if user_input == "report":
            print_resource()
        elif user_input in MENU.keys():
            check_resource(user_input)


# TODO 2. Check for the resources
def check_resource(user_input):
    """This function checks for the resources"""
    for key in MENU[user_input]["ingredients"]:
        if not (MENU[user_input]["ingredients"][key] <= resources[key]):
            print(f"Sorry there is not enough {key}.")
            return
    insert_coins(user_input)


# TODO 3. Print available resources
def print_resource():
    """This function prints the available resources"""
    for key in resources:
        print(f"{key}: {resources[key]}")


# TODO 4. Insert the coins
def insert_coins(user_input):
    """This function asks the users to insert the coins"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    check_transaction_and_change(total_value, user_input)


# TODO 5. Check if the transaction is sufficient
def check_transaction_and_change(total_value, user_input):
    """This function checks if the coins inserted by the user is sufficient or excess"""
    if total_value > MENU[user_input]["cost"]:
        change_calculate = total_value - MENU[user_input]["cost"]
        print(f"Here is ${round(change_calculate, 2)} dollars in change.")
        add_to_total(user_input)
        return
    elif total_value == MENU[user_input]["cost"]:
        add_to_total(user_input)
        return
    elif total_value < MENU[user_input]["cost"]:
        print(f"Sorry that's not enough money. Money refunded")
        return


# TODO 6. Add inserted coins to total
def add_to_total(user_input):
    """This function is used to add coins to the total"""
    resources["money"] += MENU[user_input]["cost"]
    deduct_resources(user_input)


# TODO 7. Deduct resources
def deduct_resources(user_input):
    """This function is used to deduct resources based on the user input"""
    for resource in MENU[user_input]["ingredients"]:
        resources[resource] -= MENU[user_input]["ingredients"][resource]
    print(f"Here is your {user_input} Enjoy!")


coffee_user_interface()
